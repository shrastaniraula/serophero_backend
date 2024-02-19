from django.contrib import admin
from communications.models import Suggestions

class SuggestionsAdmin(admin.ModelAdmin):
    list_display = ['by', 'description', 'datetime']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'to', 'created', 'message', 'image']

admin.site.register(Suggestions, SuggestionsAdmin)
