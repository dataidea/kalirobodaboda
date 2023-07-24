from . import views
from django.urls import path

# set application name for urls
app_name = 'accounts'

urlpatterns = [
    path(route='profile', view=views.profile, name='profile'),
    path(route='member_table', view=views.memberTable, name='member_table'),
    path(route='member_search', view=views.memberSearch, name='member_search')
]
