import csv
from .models import Member
from django.contrib import admin
from django.http import HttpResponse
from datetime import datetime


# Custom MemberAdmin to display specific attributes


class MemberAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'first_name', 'last_name', 'title',
                    'stage', 'village', 'district', 'phone_number')

    list_filter = ['title', 'status', 'stage', 'village', 'district']

    def import_members(modeladmin, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="members.csv"'

        writer = csv.writer(response)
        writer.writerow(['first_name', 'last_name', 'email', 'title', 'gender', 'phone_number',
                        'display_picture', 'district', 'village', 'stage', 'card_id', 'issue_date', 'expiry_date'])

        for member in queryset:
            writer.writerow([member.first_name, member.last_name, member.email, member.title, member.gender, member.phone_number,
                            member.display_picture, member.district, member.village, member.stage, member.card_id, member.issue_date, member.expiry_date])

        return response

    import_members.short_description = "Import selected members to CSV"


# Register your models here.
admin.site.register(Member, MemberAdmin)

# modify admin
admin.site.site_header = "Kaliro Boda Association"
admin.site.site_title = "Kaliro Boda Association Admin"
