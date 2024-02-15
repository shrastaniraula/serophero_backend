from django.contrib import admin

from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description','by','location','event_date','post_date')
    search_fields = ('title','description','by','location')
    list_filter = ('event_date','post_date')

admin.site.register(Event, EventAdmin)
