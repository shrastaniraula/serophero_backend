from django.contrib import admin
from communications.models import Message, Suggestions

class SuggestionsAdmin(admin.ModelAdmin):
    list_display = ['by', 'description', 'datetime']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'created', 'message', 'image']

admin.site.register(Suggestions, SuggestionsAdmin)
admin.site.register(Message, MessageAdmin)

