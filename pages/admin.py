from django.contrib import admin

# Register your models here.
from .models import Member

from django.utils.html import format_html
class MemberAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src ="{}" width=40 style="border-radius: 40px" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'ocuppation', 'created_date',)
    list_display_links = ('id', 'thumbnail', 'first_name',)
    search_fields = ('first_name', 'last_name', 'ocuppation',)
    list_filter = ('last_name', 'ocuppation',)


admin.site.register(Member, MemberAdmin)
