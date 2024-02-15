from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from user.models import User
from .models import Event


class CreateEventView(APIView):
    def post(self, request):
        title = request.data['title']
        description = request.data['description']
        event_image = request.FILES['event_image']
        event_date = request.data['event_date']
        by = request.data['by']
        allowed_members = request.data['allowed_members']
        location = request.data['location']


        print(title, by, event_date, allowed_members)
        user_instance = User.objects.get(id=by)

        allowed_members_list = User.objects.filter(id__in=allowed_members)
        # allowed_members_list = []
        # for each in allowed_members:
        #     print(f"\n\n{each}\n\n")
        #     users_objects = User.objects.get(id=each)
        #     allowed_members_list.append(users_objects)



        event = Event.objects.create(
            title=title,
            description=description,
            by=user_instance,
            location= location,
            event_date = event_date,
            event_image = event_image
        )
        if event: 
            event.allowed_members.set(allowed_members_list)
            event.save()
            return Response({'success': 'Event posted successfully'})

        else:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        
class RetrieveView(APIView):
    def post(self, request):
        user = request.data['user']
        events = Event.objects.filter(allowed_members= user)

        return Response({'success': 'Success','events': events})



