from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Member


class MemberAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src ={} width=40 style="border-radius: 40px;" />'.format(
                object.photo.url
            )
        )

    thumbnail.short_description = "Photo"
    list_display = (
        "id",
        "thumbnail",
        "first_name",
        "last_name",
        "ocuppation",
        "created_date",
    )
    list_display_links = (
        "id",
        "thumbnail",
        "first_name",
    )
    search_fields = (
        "first_name",
        "last_name",
        "ocuppation",
    )
    list_filter = (
        "last_name",
        "ocuppation",
    )


admin.site.register(Member, MemberAdmin)
