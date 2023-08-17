import csv
from .models import Member
from django.contrib import admin
from django.http import HttpResponse


# Custom MemberAdmin to display specific attributes


class MemberAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'first_name', 'last_name', 'title',
                    'stage', 'village', 'district', 'phone_number')

    list_filter = ['title', 'status', 'stage', 'village', 'district']

    search_fields = ['card_id', 'first_name',
                     'last_name', 'title', 'phone_number']


# Register your models here.
admin.site.register(Member, MemberAdmin)
