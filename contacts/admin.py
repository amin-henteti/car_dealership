from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'car_id',  'first_name', 'last_name', 'email', 'phone', 'customer_need', 'car_id', 'created_date')
    list_display_links = ('id', 'user_id', 'car_id', 'first_name', 'last_name',)
    search_fields = ('first_name', 'last_name', 'email', 'car_id')
    
admin.site.register(Contact, ContactAdmin)
