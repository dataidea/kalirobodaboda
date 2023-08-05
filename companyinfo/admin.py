from .models import Leader
from .models import Service
from .models import CompanyInfo
from django.contrib import admin
from .models import FrequentlyAskedQuestion


class LeaderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'title']


# Register your models here.
admin.site.register(Service)
admin.site.register(Leader, LeaderAdmin)
admin.site.register(CompanyInfo)
admin.site.register(FrequentlyAskedQuestion)

# modify admin
# get compnay info


def fetchCompanyInfo():
    try:
        company_info = CompanyInfo.objects.values()[0]
        print({'company_info': company_info})
    except Exception as e:
        company_info = {}
    return company_info


comapny_info = fetchCompanyInfo()

admin.site.site_header = f'{comapny_info["name"]}'
admin.site.site_title = f'{comapny_info["name"]} Admin'
