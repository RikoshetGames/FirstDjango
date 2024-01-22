from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))