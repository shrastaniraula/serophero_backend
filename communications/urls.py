from django.urls import path
from .views import MessageListView, SuggestionsView

urlpatterns = [
    path('message_list/', MessageListView.as_view()),
    path('suggestions/', SuggestionsView.as_view()),

]