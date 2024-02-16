from django.contrib import admin
from reports.models import Blacklist, Report, Warning

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason', 'by', 'reported_date', 'post')
    search_fields = ('user__username', 'by__username')
    list_filter = ('reported_date',)

class WarningAdmin(admin.ModelAdmin):
    list_display= ('warning_date', 'message', 'user_warned')

class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('user', 'blacklisted_date')


admin.site.register(Report, ReportAdmin)
admin.site.register(Warning, WarningAdmin)
admin.site.register(Blacklist, BlacklistAdmin)

