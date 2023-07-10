from django.contrib import admin
from .models import User
from .models import Member

# Register your models here.
admin.site.register(model_or_iterable=[User, Member])

# modify admin
admin.site.site_header = "Kaliro Boda Association"
admin.site.site_title = "Kaliro Boda Association Admin"