from django.urls import path
from .views import MessageListView

urlpatterns = [
    path('message_list/', MessageListView.as_view()),

]