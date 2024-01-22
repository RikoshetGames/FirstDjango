from django.urls import path
from users.apps import UsersConfig
from users.views import logout_view
from django.contrib.auth.views import LoginView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]