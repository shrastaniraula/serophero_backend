from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'amount', 'receiver', 'sender', 'payment_datetime']
    search_fields = ['transaction_id', 'remarks']
    list_filter = ['payment_datetime']
    # You can customize further according to your requirements

admin.site.register(Payment, PaymentAdmin)
