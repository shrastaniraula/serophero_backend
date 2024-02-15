from django.urls import path
from .views import LoginView, OTPView, RegisterView, TokenView
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/', TokenView.as_view()),
    path('otp/', OTPView.as_view()),
]