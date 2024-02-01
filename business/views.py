from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Business
from user.models import User
from .serializers import BusinessSerializer, UserSerializer

class RegisterBusinessView(APIView):

    def post(self, request):
        
        serializer = BusinessSerializer(data=request.data)

        if serializer.is_valid():
            business = serializer.save()
            business.save()

            return Response({'Business registration': 'Business is regsitered. You will be informed about verification later'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllUsersBusiness(APIView):
    def get(self, request):
        users = User.objects.all()
        user_business_data = []

        
        for user in users:
            
            try:
                business = Business.objects.get(user=user)
                business_serializer = BusinessSerializer(business)
            except Business.DoesNotExist:
                business_serializer = None
                
            user_seriliazers=UserSerializer(user)

            user_data = {
                "user": user_seriliazers.data,
                "business": business_serializer.data if business_serializer else None,
            }

            user_business_data.append(user_data)

        return Response(user_business_data, status=status.HTTP_200_OK)