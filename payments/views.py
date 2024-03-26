from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from payments.models import Payment
from payments.serializers import PaymentSerializer
from user.models import User


class PaymentView(APIView):
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            print("helloo")
            token = request.data['token']
            trans = request.data['transaction_id']
            amount = request.data['amount']
            user_id = request.data['user_id']
            remarks = request.data['remarks']

            receiver = User.objects.get(id=user_id)
            payment = Payment.objects.create(
                    token=token,
                    transaction_id=trans,
                    amount=amount,
                    receiver=receiver,
                    sender=user, 
                    remarks=remarks
                )


            print(token, trans, amount, user_id, remarks)
            return Response("serialized_news_data")
        else:
            print("not right")


class PaymentHistoryView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            data = Payment.objects.filter(sender = user)
            serialized_data = PaymentSerializer(data, many = True).data

            return Response(serialized_data)

