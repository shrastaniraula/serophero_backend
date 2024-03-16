from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()
    event_title = serializers.CharField()
    event_description = serializers.CharField()
    event_image = serializers.CharField()
    event_location = serializers.CharField()
    posted_date = serializers.DateTimeField()
    event_date = serializers.DateTimeField()
    posted_by = serializers.CharField()
    user_id = serializers.CharField()