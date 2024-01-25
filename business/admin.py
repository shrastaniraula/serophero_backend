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

class BusinessAdminForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    def clean_images(self):
        images = self.cleaned_data.get('images', [])
        return [image for image in images]

class BusinessAdmin(admin.ModelAdmin):
    form = BusinessAdminForm
    list_display = ('name', 'is_verified', 'user')

    def save_model(self, request, obj, form, change):
        # Process the images before saving the model
        images = form.cleaned_data.get('images', [])
        obj.images = images
        super().save_model(request, obj, form, change)

admin.site.register(Business, BusinessAdmin)
