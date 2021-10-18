from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Car


class CarsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src={}  width=66 style="border-radius: 10px"'.format(
                object.main_image.url
            )
        )

    thumbnail.short_description = "Photo"
    list_display = (
        "id",
        "title",
        "thumbnail",
        "price",
        "miles",
        "year",
        "availibility",
        "created_date",
    )
    list_display_links = (
        "id",
        "title",
        "thumbnail",
    )
    search_fields = ("title", "model", "provinance", "description", "color")
    list_filter = ("color", "availibility")
    list_editable = ("availibility",)


admin.site.register(Car, CarsAdmin)
