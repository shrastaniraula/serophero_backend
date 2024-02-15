from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_heading','news_description','author','news_image','post_date','is_verified')
    search_fields = ('news_heading','news_description','author')
    list_filter = ('is_verified','post_date')

admin.site.register(News, NewsAdmin)

