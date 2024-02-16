from django.contrib import admin
from business.models import Business
from .models import User, Report

class ReportInline(admin.StackedInline):
    model = Report
    extra = 1
    fk_name = 'user'

class BusinessInline(admin.StackedInline):  # or admin.TabularInline for a more compact view
    model = Business
    extra = 1 

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'user_type', 'report_count', 'blacklisted')
    search_fields = ('username', 'email')
    list_filter = ('user_type', 'blacklisted')
    inlines = [BusinessInline, ReportInline]
    readonly_fields = ('display_image',)

    fieldsets = [
        ('Personal information', {'fields': ['first_name', 'last_name', 'email', 'address', 'image']}),
        ('Account information', {'fields': ['username', 'password', "phone_no"]}),
        ('User choice information', {'fields': ['user_type', 'authority_role', 'is_active', 'is_superuser', 'is_staff']}),
        ('Reports and blacklists', {'fields': ['report_count', 'blacklisted']}),
        ('Groups and Permissions', {'fields': ['groups', 'user_permissions']})
    ]

# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('user', 'reason', 'by', 'reported_date')
#     search_fields = ('user__username', 'by__username')
#     list_filter = ('reported_date',)

# Register your models with the admin site
admin.site.register(User, UserAdmin)
# admin.site.register(Report, ReportAdmin)
