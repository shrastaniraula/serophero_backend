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

            otp = send_otp(request)
            message = f" Your otp for registration continuation is {otp}."
            send_email(request, [serializer.validated_data['email']], message)
            
            request.session['username'] = user.username
            return Response({'verification_code': 'Enter verification code for successful registeration.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OTPView(APIView):
    def post(self, request):
        otp = request.data['entered_otp']
        username = request.session['username']

        otp_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']


        if otp_key is not None and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)
            
            print(valid_until)
            print(datetime.now())
            if valid_until > datetime.now():
                print("inside datetime")
                totp = pyotp.TOTP(otp_key, interval= 60)
                if totp.verify(otp):
                    print("inside verification")
                    user = User.objects.get(username= username)
                    user.is_active = True
                    user.save()
                    return Response({"success": "successful registration"})
                
        return Response({"nothing"})



class TokenView(APIView):
    permission_classes=[IsAuthenticated]
    
    # @login_required
    def get(self, request):
        return Response({'hii': 'good job'})
