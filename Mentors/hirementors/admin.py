from django.contrib import admin
from .models import Hirementor
# Register your models here.


class HireMentorAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'mentor_name']


admin.site.register(Hirementor, HireMentorAdmin)
