from .models import Member
from django.contrib import admin

# Custom MemberAdmin to display specific attributes


class MemberAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'first_name', 'last_name', 'title',
                    'stage', 'village', 'district', 'phone_number')


# Register your models here.
admin.site.register(Member, MemberAdmin)

# modify admin
admin.site.site_header = "Kaliro Boda Association"
admin.site.site_title = "Kaliro Boda Association Admin"
