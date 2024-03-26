from rest_framework import serializers
from .models import Payment
# from django.contrib.auth.models import User

class PaymentSerializer(serializers.ModelSerializer):
    receiver_name = serializers.SerializerMethodField()
    receiver_contact = serializers.SerializerMethodField()

    def get_receiver_name(self, obj):
        return f"{obj.receiver.first_name} {obj.receiver.last_name}"

    def get_receiver_contact(self, obj):
        return obj.receiver.phone_no

    class Meta:
        model = Payment
        fields = ['token', 'transaction_id', 'amount', 'receiver', 'receiver_name', 'receiver_contact', 'remarks', 'payment_datetime']
