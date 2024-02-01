from django.urls import path
from .views import AllUsersBusiness, RegisterBusinessView

urlpatterns = [
    path('register/', RegisterBusinessView.as_view()),
    path('directories/', AllUsersBusiness.as_view()),

]