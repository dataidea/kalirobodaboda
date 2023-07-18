from django.contrib import admin
from .models import User
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member


class UserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'gender', 'display_picture'),
        }),
    )

# Custom MemberAdmin to display specific attributes


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_id', 'stage', 'phone_number')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)

# modify admin
admin.site.site_header = "Kaliro Boda Association"
admin.site.site_title = "Kaliro Boda Association Admin"
