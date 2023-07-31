from django.contrib import admin
from .models import CompanyInfo
from .models import Service
from .models import FrequentlyAskedQuestion

# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(Service)
admin.site.register(FrequentlyAskedQuestion)
