from datetime import datetime
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
from .serializers import RegisterSerializer, UserDetailsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

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
        # if user.is_authenticated:
        print(user)
        # user_obj=User.objects.get(email=user)
        user = str(user)
        
        return Response({"userName": user})
        # else:
        #     return Response({"userName": "hello"})

class VisitProfile(APIView):
    def post(self, request):
        logged_user = request.user
        user = request.data['user']
        view_profile_details = []

        if logged_user.is_authenticated:
            user_details = User.objects.get(id = user)
            business_details = Business.objects.filter(user = user_details).first()
            if business_details:
                view_profile_details.append({"user_id": user_details.id,
                                            "user_fullname": f"{user_details.first_name} {user_details.last_name}",
                                            "user_name": user_details.username,
                                            "user_location": user_details.address,
                                            "user_contact": user_details.phone_no,
                                            "user_email": user_details.email,
                                            "user_image": user_details.image,
                                            "user_type": user_details.user_type,
                                            "authority_role": user_details.authority_role,
                                            "business_name": business_details.name,
                                            "business_description": business_details.description
                                            })
            else:
                view_profile_details.append({"user_id": user_details.id,
                                            "user_fullname": f"{user_details.first_name} {user_details.last_name}",
                                            "user_name": user_details.username,
                                            "user_location": user_details.address,
                                            "user_contact": user_details.phone_no,
                                            "user_email": user_details.email,
                                            "user_image": user_details.image,
                                            "user_type": user_details.user_type,
                                            "authority_role": user_details.authority_role,
                                            "business_name": "",
                                            "business_description": ""
                                            })
            serialized_view_profile_data = UserDetailsSerializer(view_profile_details, many=True).data
            return Response(serialized_view_profile_data)


            

