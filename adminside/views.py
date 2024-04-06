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
from adminside.serializers import BusinessAdminSerializer, NewsAdminSerializer, UserAdminSerializer
from business.models import Business
from news.models import News
from user.models import MobileTokens, User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class LoginAdminView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            update_last_login(user, user)
        
            return Response({ 'refresh_token':refresh_token, 'access_token': access_token }, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



class UserAdminView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            users = User.objects.exclude(id=request.user.id)
            serialized_data = UserAdminSerializer(users, many= True).data
            return Response(serialized_data)
            
            

    def post(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass

class NewsAdminView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            news = News.objects.all()
            serialized_data = NewsAdminSerializer(news, many= True).data
            return Response(serialized_data)

    def patch(self, request):
        pass

class BusinessAdminView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            businesses = Business.objects.all()
            serialized_data = BusinessAdminSerializer(businesses, many= True).data
            return Response(serialized_data)

    def patch(self, request):
        pass

class HomeAdminView(APIView):
    def get(self, request):
        pass