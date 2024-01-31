from datetime import datetime
import pyotp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.models import update_last_login
from user.models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

from .utils import send_email, send_otp

class LoginView(APIView):

    def post(self, request):
            username = request.data['username']
            password = request.data['password']

            print(username, password)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)

                response_data ={
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }

                update_last_login(user, user)
                return Response({'token': response_data}, status=status.HTTP_200_OK)

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



        # if otp_key is not None and otp_valid_until is not None:
        if otp_key is not None:
            # print("inside otp")
            # valid_until = datetime.fromisoformat(otp_valid_until)
            # print(valid_until)
            # print(datetime.now())
            # if valid_until > datetime.now():
            #     print("inside datetime")
            totp = pyotp.TOTP(otp_key, interval= 120)
            if totp.verify(otp):
                # print("inside verification")
                user = User.objects.get(email= sess_email)
                user.is_active = True
                user.save()
                return Response({"success": "successful registration"})
            else:
                return Response({"error": "Wrong OTP or time out."})

                
        return Response({"error": "Sorry, something went wrong."})

# class OTPView(APIView):
#     def post(self, request):
#         otp = request.data['entered_otp']
#         email = request.data['email']

        
#         if otp == "correct":
            
#             print(datetime.now())
#             user = User.objects.get(email= email)
#             user.is_active = True
#             user.save()
#             return Response({"success": "successful registration"})
                
#         return Response({"nothing"})



class TokenView(APIView):
    permission_classes=[IsAuthenticated]
    
    # @login_required
    def get(self, request):
        return Response({'hii': 'good job'})
