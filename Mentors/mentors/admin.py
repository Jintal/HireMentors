from django.contrib import admin
from django.utils.html import format_html
from .models import Mentor

# Register your models here.


class MentorAdmin(admin.ModelAdmin):
    def my_photo(self, object):
        return format_html('<img src = "{}" width="70"/>'.format(object.photo.url))

    list_display = ('id', 'my_photo', 'first_name', 'is_featured')
    search_fields = ('category', 'camera_type', 'first_name', 'last_name')
    list_filter = ('city', 'category', 'camera_type')
    list_display_links = ('id', 'first_name')

    # Makes the fields editabel in admin panel
    list_editable = ('is_featured',)


admin.site.register(Mentor, MentorAdmin)
