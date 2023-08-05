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
