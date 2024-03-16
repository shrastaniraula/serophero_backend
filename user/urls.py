from django.urls import path
from .views import LoginView, OTPView, RegisterView, HomeView, VisitProfile
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('otp/', OTPView.as_view()),
    path('home/', HomeView.as_view()),
    path('view_profile/', VisitProfile.as_view()),


]