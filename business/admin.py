# from django.contrib import admin
# from .models import Business

# class BusinessAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_verified', 'user')
#     fields = ('name', 'images', 'description', 'is_verified', 'user')  # Include 'images' here
#     # search_fields = ('name')
#     # list_filter = ('is_verified')


# admin.site.register(Business, BusinessAdmin)

from django import forms
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from .models import Business

# class BusinessAdminForm(forms.ModelForm):
#     class Meta:
#         model = Business
#         fields = '__all__'

#     images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


class BusinessAdmin(admin.ModelAdmin):
    # form = BusinessAdminForm
    list_display = ('name','description', 'is_verified', 'user')
    list_filter = ('is_verified',)


    # def save_model(self, request, obj, form, change):
    #     # Process the images before saving the model
    #     images = form.cleaned_data.get('images', [])
    #     obj.images = images
    #     super().save_model(request, obj, form, change)

admin.site.register(Business, BusinessAdmin)
