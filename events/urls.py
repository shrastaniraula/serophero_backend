from django.urls import path
from .views import CreateEventView, RetrieveView
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('post_event/', CreateEventView.as_view()),
    path('fetch_event/', RetrieveView.as_view()),
]