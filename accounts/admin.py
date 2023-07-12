from django.contrib import admin
from .models import User
from .models import Member
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name')

# Custom MemberAdmin to display specific attributes
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_id', 'stage', 'phone_number')

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Member, MemberAdmin)

# modify admin
admin.site.site_header = "Kaliro Boda Association"
admin.site.site_title = "Kaliro Boda Association Admin"