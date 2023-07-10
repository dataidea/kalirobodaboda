from django.contrib import admin
from .models import District
from .models import Stage
from .models import Village

# Register your models here.
admin.site.register(model_or_iterable=[District, Stage, Village])
