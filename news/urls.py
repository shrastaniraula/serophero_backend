from django.urls import path
from .views import NewsView, PostNewsView

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('news_add/', PostNewsView.as_view()),


]