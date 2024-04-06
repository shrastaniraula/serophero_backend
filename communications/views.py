from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from communications.models import Message, Suggestions
from communications.serializers import MessageListSerializer, MessageSerializer, SuggestionsSerializer
from user.models import User
from rest_framework import status



class SuggestionsView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.user_type == "authority":
                suggestions = Suggestions.objects.all()
                print(suggestions)
                serialized_data = SuggestionsSerializer(suggestions,many=True).data
                return Response(serialized_data)
            else:
                return Response({"error": "Sorry, only for authority man"}, status= status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        user = request.user
        description = request.data['description']
        try:
            if user.is_authenticated:
                suggestion = Suggestions.objects.create(by = user, description= description)
                return Response({"success": "Your suggestion is dropped successfully."})
            

        except:
                return Response({"error": "Seems like the fields are missing"})
        
class MessageListView(APIView):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            # user_obj = User.objects.get(email = user)
            messages = Message.objects.filter(
            Q(to=request.user) | Q(user=request.user)
        ).order_by('-created')

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        email_user = request.user

        if email_user.is_authenticated:
            users = User.objects.exclude(email=email_user.email).filter(
            Q(sent_messages__receiver=request.user) | Q(received_messages__sender=request.user) |
            Q(sent_messages__sender=request.user) | Q(received_messages__receiver=request.user)
            ).distinct()
        

            # Get the latest message for each chat
            message_list = []
            for user in users:
                latest_message = Message.objects.filter(
                    Q(sender=email_user, receiver=user) | Q(sender=user, receiver=email_user)
                ).latest('created')

                # Determine if the message is sent by the logged-in user
                is_sent = latest_message.sender == email_user

                message_list.append({"user_email": user.email,
                                    "user_image": user.image,
                                    "user_fullname": f"{user.first_name} {user.last_name}", 
                                    "my_id": email_user.id,
                                    "user_id": user.id,
                                    "latest_message": latest_message.message, 
                                    "datetime": latest_message.created,
                                    "sent_by_me": is_sent
                                    })
            

            message_list_serializer = MessageListSerializer(message_list, many = True).data
            return Response(message_list_serializer)


    

