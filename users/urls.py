from django.urls import path
from users.apps import UsersConfig
from users.views import logout_view, RegisterView, ProfileView, confirm_registration, invalid_token_view, generate_new_password, reset_password
from django.contrib.auth.views import LoginView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('confirm-registration/<str:token>/', confirm_registration, name='confirm_registration'),
    path('invalid-token/', invalid_token_view, name='invalid_token'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
    path('reset_password/', reset_password, name='reset_password'),
]
