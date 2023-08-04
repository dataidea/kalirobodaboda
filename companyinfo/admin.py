from .models import Leader
from .models import Service
from .models import CompanyInfo
from django.contrib import admin
from .models import FrequentlyAskedQuestion

# Register your models here.
admin.site.register(Service)
admin.site.register(Leader)
admin.site.register(CompanyInfo)
admin.site.register(FrequentlyAskedQuestion)
