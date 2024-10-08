from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Business
from user.models import User
from .serializers import BusinessUserSerializer
from user.serializers import UserSerializer

class RegisterBusinessView(APIView):

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            citizen_front = request.FILES['citiz_front_image']
            citizen_back = request.FILES['citiz_back_image']
            docs1 = request.FILES['optional_docs1_image']
            docs2 = request.FILES['optional_docs2_image']
            docs3 = request.FILES['optional_docs3_image']
            name = request.data['name']
            description = request.data['description']

    
            object = Business.objects.create(user=user, name = name, description=description, citiz_front_image =citizen_front, citiz_back_image= citizen_back,optional_docs1_image= docs1,optional_docs2_image= docs2,optional_docs3_image= docs3 )
            if object:
                object.save()
                return Response({'success': 'Business is regsitered. You will be informed about verification later'})
            else:
                # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response( status=status.HTTP_400_BAD_REQUEST)



class AllUsersBusiness(APIView):
    def get(self, request):
        users = User.objects.exclude(id=request.user.id).exclude(is_superuser=True).exclude(is_staff=True)

        user_business_data = []

        for user in users:
            business = Business.objects.filter(user=user, is_verified=True).first()
            user_data = {
                "user_id": user.id,
                "user_name": f"{user.first_name} {user.last_name}",
                "user_image": user.image,
                "user_type": user.user_type,
                "business_name": business.name if business else "",
                "business_desc": business.description if business else "",
                "business_date": business.created_at if business else ""

            }
            user_business_data.append(user_data)

        # Serialize the user business data
        serialized_user_business_data = BusinessUserSerializer(user_business_data, many=True).data

        return Response(serialized_user_business_data)