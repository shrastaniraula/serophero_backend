from django.urls import path
from .views import PaymentHistoryView, PaymentView

urlpatterns = [
    path('make_payment/', PaymentView.as_view()),
    path('payment_history/', PaymentHistoryView.as_view()),


]