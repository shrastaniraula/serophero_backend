from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['by', 'title', 'description', 'event_image', 'event_date', 'post_date', 'location', 'allowed_members']