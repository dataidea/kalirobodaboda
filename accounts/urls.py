from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path(route='signin', view=views.signin, name='signin'),
    path(route='signup', view=views.signup, name='signup'),
    path(route='forgot_password', view=views.forgot_password, name='forgot_password')
]