from django.urls import path
from .views import BusinessAdminView, LoginAdminView, NewsAdminView, UserAdminView
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('login/', LoginAdminView.as_view()),
    path('users/', UserAdminView.as_view()),
    path('news/', NewsAdminView.as_view()),
    path('business/', BusinessAdminView.as_view()),
]