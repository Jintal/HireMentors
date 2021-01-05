from django.contrib import admin
from django.utils.html import format_html

from .models import Slider, Team
# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    def my_photo(self, object):
        return format_html('<img src = "{}" width="500"/>'.format(object.photo.url))
    list_display = ['headline', 'my_photo', 'button_text']


class TeamAdmin(admin.ModelAdmin):

    def my_photo(self, object):
        return format_html('<img src = "{}" width="40"/>'.format(object.photo.url))

    def format_name(self, object):
        return format_html('<strong>{}</strong>'.format(object.first_name))

    def company_name(self, object):
        return format_html('<p>Robot Inc.</p>')

    list_display = ('id', 'my_photo', 'format_name', 'company_name',
                    'first_name', 'last_name', 'role', 'created_date')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
