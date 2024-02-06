from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Business
from user.models import User
from .serializers import BusinessSerializer, UserSerializer, BusinessRegisterSerializer

class RegisterBusinessView(APIView):

    def post(self, request):
        citizen_front = request.FILES['citiz_front_image']
        citizen_back = request.FILES['citiz_back_image']
        docs1 = request.FILES['optional_docs1_image']
        docs2 = request.FILES['optional_docs2_image']
        docs3 = request.FILES['optional_docs3_image']
        name = request.data['name']
        description = request.data['description']
        user = request.data['user']

        print(request.data)
        user_instance = User.objects.get(id=user)
        object = Business.objects.create(user=user_instance, name = name, description=description, citiz_front_image =citizen_front, citiz_back_image= citizen_back,optional_docs1_image= docs1,optional_docs2_image= docs2,optional_docs3_image= docs3 )
        if object:
            object.save()
        # serializer = BusinessRegisterSerializer(data=request.data)

        # print(serializer)
        # if serializer.is_valid():
        #     business = serializer.save()
        #     business.save()

            return Response({'success': 'Business is regsitered. You will be informed about verification later'})
        else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response( status=status.HTTP_400_BAD_REQUEST)



class AllUsersBusiness(APIView):
    def post(self, request):
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
            print(user_data)

            user_business_data.append(user_data)

        return Response(user_business_data, status=status.HTTP_200_OK)