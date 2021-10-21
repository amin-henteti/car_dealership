from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'customer_need', 'car_id')
    list_display_links = ('first_name', 'last_name', 'car_id')
    search_fields = ('first_name', 'last_name', 'email', 'car_id')
    
admin.site.register(Contact, ContactAdmin)
