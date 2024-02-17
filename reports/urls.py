from django.urls import path
from reports.views import ReportView


urlpatterns = [
    path('report/', ReportView.as_view()),

]