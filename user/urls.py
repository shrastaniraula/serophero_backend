from django.urls import path
from .views import LoginView, LogoutView, OTPView, RegisterView, HomeView, ResetPassword, UpdateProfile, VisitProfile
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('otp/', OTPView.as_view()),
    path('home/', HomeView.as_view()),
    path('view_profile/', VisitProfile.as_view()),
    path('update_profile/', UpdateProfile.as_view()),
    path('pass_reset_email/', ResetPassword.as_view()),
    # path('change_password/', UpdateProfile.as_view()),

]