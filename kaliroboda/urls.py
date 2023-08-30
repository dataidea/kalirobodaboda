"""kaliroboda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# handle page not found
handler404 = views.pageNotFound
# handle server error
handler500 = views.serverError

urlpatterns = [
    path(route='', view=views.dashbord, name='dashbord'),
    path(route='accounts/', view=include('accounts.urls')),
    path(route='admin/', view=admin.site.urls),
    path(route='home/', view=views.home, name='home'),
    path(route='export/', view=views.export_csv, name='export'),
    path(route='faqs', view=views.faqs, name='faqs'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
