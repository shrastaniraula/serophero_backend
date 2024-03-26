import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from events.serializers import EventSerializer
from user.models import User
from .models import Event
import ast



class CreateEventView(APIView):
    def post(self, request):
        user = request.user
        if user.is_authenticated:

            title = request.data['title']
            description = request.data['description']
            event_image = request.FILES['event_image']
            event_date = request.data['event_date']
            allowed_members = request.data['allowed_members']
            location = request.data['location']

            print(title, event_date, allowed_members)

            print(type(event_date))

            event = Event.objects.create(
                title=title,
                description=description,
                by=user,
                location= location,
                event_date = event_date,
                event_image = event_image
            )

            allowed_members_list = json.loads(allowed_members)

            print(allowed_members_list)

            allowed_members_objs = User.objects.filter(id__in=allowed_members_list)
            if event: 
                event.allowed_members.set(allowed_members_objs)
                event.save()
                return Response({'success': 'Event posted successfully'})

        
class RetrieveView(APIView):
    def get(self, request):
        user = request.user
        event_data = []

        if user.is_authenticated:
            
            events = Event.objects.filter(allowed_members=user)
            
            for event in events:
                event_posted_by = User.objects.get(email = event.by)
                event_data.append({
                    "event_id": event.id,
                    "event_title": event.title,
                    "event_description": event.description,
                    "event_date": event.event_date,
                    "posted_date": event.post_date,
                    "event_image": f"media/{event.event_image}",
                    "event_location": event.location,
                    "posted_by": f"{event_posted_by.first_name} {event_posted_by.last_name}",
                    "user_id": event_posted_by.id
                })
            
            serialized_event_data = EventSerializer(event_data, many= True).data
            return Response(serialized_event_data)
            
