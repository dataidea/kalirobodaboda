from . import views
from django.urls import path

# set application name for urls
app_name = 'accounts'

urlpatterns = [
    path(route='signin', view=views.signin, name='signin'),
    path(route='signup', view=views.signup, name='signup'),
    path(route='settings', view=views.settings, name='settings'),
    path(route='signout', view=views.signout, name='signout'),
    path(route='profile', view=views.profile, name='profile'),
    path(route='forgot_password', view=views.forgotPassword, name='forgot_password'),
    path(route='user_table', view=views.userTable, name='user_table'),
    path(route='user_search', view=views.userSearch, name='user_search')
]
