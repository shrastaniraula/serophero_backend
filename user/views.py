# from datetime import datetime
from django.utils import timezone
import json
import pyotp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.models import update_last_login
from business.models import Business
from user.models import User
from .serializers import CombinedHomeSerializer, RegisterSerializer, UserDetailsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from events.models import Event


from .utils import send_email, send_otp

class LoginView(APIView):

    def post(self, request):
            email = request.data['email']
            password = request.data['password']

            print(email, password)

            user = authenticate(request, username=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                refresh_token = str(refresh)
                access_token = str(refresh.access_token)


                update_last_login(user, user)
                return Response({ 'refresh_token':refresh_token, 'access_token': access_token }, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):

    def post(self, request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            # Hash the password
            user.set_password(serializer.validated_data['password'])
            user.save()

            otp, otp_key = send_otp(request)
            message = f" Your otp for registration continuation is {otp}."
            subject = "OTP code verification"
            email = serializer.validated_data['email']
            send_email(request, [email], message, subject)
            print (otp)
            
            
            return Response({'success': 'Enter verification code for successful registeration.', 'otp_key': otp_key, 'email': email })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPView(APIView):
    def post(self, request):
        otp = request.data['entered_otp']
        print(otp)
        sess_email = request.data['email']
        otp_key = request.data['otp_key']

        if otp_key is not None:
            totp = pyotp.TOTP(otp_key, interval= 600)
            if totp.verify(otp):
                # print("inside verification")
                user = User.objects.get(email= sess_email)
                user.is_active = True
                user.save()
                return Response({"success": "successful registration"})
            else:
                return Response({"error": "Wrong OTP or time out."})

                
        return Response({"error": "Sorry, something went wrong."})
    

class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            business_details = Business.objects.filter(user=user).first()
            profile_data = {
                    "user_id": user.id,
                    "user_fullname": f"{user.first_name} {user.last_name}",
                    "user_name": user.username,
                    "user_location": user.address,
                    "user_contact": user.phone_no,
                    "user_email": user.email,
                    "user_image": user.image.url if user.image else None,
                    "user_type": user.user_type,
                    "authority_role": user.authority_role if user.authority_role else "",
                    "business_name": business_details.name if business_details else "",
                    "business_description": business_details.description if business_details else ""
                }
            
            upcoming_events = Event.objects.filter(
                            allowed_members=user,
                            event_date__gt=timezone.now()  # Filter events with event date greater than current datetime
                        ).order_by('event_date')[:3]  # Limit the results to three events and order by event date
    
            event_data = []
            for event in upcoming_events:
                event_posted_by = User.objects.get(email=event.by)
                event_data.append({
                    "event_id": event.id,
                    "event_title": event.title,
                    "event_description": event.description,
                    "event_date": event.event_date,
                    "posted_date": event.post_date,
                    "event_image": f"media/{event.event_image}",
                    "event_location": event.location,
                    "posted_by": f"{event_posted_by.first_name} {event_posted_by.last_name}",
                    "user_id": event_posted_by.id
                })
            
            business_data =[]
            recent_businesses = Business.objects.filter(is_verified=True).order_by('-created_at')[:5]
            for business in recent_businesses:
                
                user_data = {
                "user_id": business.user.id,
                "user_name": f"{business.user.first_name} {business.user.last_name}",
                "user_image": business.user.image,
                "user_type": business.user.user_type,
                "business_name": business.name if business else "",
                "business_desc": business.description if business else "",
                "business_date": business.created_at if business else ""
                    }
                business_data.append(user_data)
            

            serialized_home_data = CombinedHomeSerializer({ 'user_details': profile_data,
                                    'business_details': business_data,
                                    'event_details': event_data}).data
        
        
            return Response(serialized_home_data)
        else:
            return Response({"userName": "hello"})


class VisitProfile(APIView):
    def post(self, request):
        logged_user = request.user
        user_id = request.data.get('user')  # Use get() to safely get the user ID from request data
        view_profile_details = []

        if logged_user.is_authenticated:
            try:
                user_details = User.objects.get(id=user_id)
                business_details = Business.objects.filter(user=user_details).first()

                # Create a dictionary with user details
                profile_data = {
                    "user_id": user_details.id,
                    "user_fullname": f"{user_details.first_name} {user_details.last_name}",
                    "user_name": user_details.username,
                    "user_location": user_details.address,
                    "user_contact": user_details.phone_no,
                    "user_email": user_details.email,
                    "user_image": user_details.image.url if user_details.image else None,  # Assuming image is a FileField or ImageField
                    "user_type": user_details.user_type,
                    "authority_role": user_details.authority_role if user_details.authority_role else "",
                    "business_name": business_details.name if business_details else "",
                    "business_description": business_details.description if business_details else ""
                }
                view_profile_details.append(profile_data)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)

            # Serialize the user profile data
            serialized_view_profile_data = UserDetailsSerializer(view_profile_details, many=True).data

            return Response(serialized_view_profile_data)
        else:
            return Response({'error': 'User not authenticated'}, status=401)

            

