from django.contrib import admin

from news.models import News
from reports.models import Report

class ReportInline(admin.StackedInline):
    model = Report
    extra = 1
    fk_name = 'post'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','news_heading','news_description','author','report_count','post_date','is_verified')
    search_fields = ('news_heading','news_description','author')
    list_filter = ('is_verified','post_date')
    inlines = [ReportInline]

admin.site.register(News, NewsAdmin)

