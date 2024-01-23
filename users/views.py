from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.template.loader import render_to_string
from django.contrib import messages

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()

        # Создание ссылки подтверждения регистрации
        confirmation_url = self.request.build_absolute_uri(reverse('users:confirm_registration', args=[new_user.email_confirmation_token]))

        # Создание HTML-содержимого письма
        message = render_to_string('users/confirmation_email.html', {
            'user': new_user,
            'confirmation_url': confirmation_url,
        })

        # Отправка письма
        send_mail(
            subject='Подтверждение регистрации',
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            html_message=message
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user



def confirm_registration(request, token):
    try:
        user = User.objects.get(email_confirmation_token=token)
        user.email_confirmation_token = None
        user.is_active = True
        user.save()
        messages.success(request, 'Ваша почта подтверждена! Можете войти в свой профиль.')
        return redirect('users:login')
    except User.DoesNotExist:
        messages.error(request, 'Недействительный токен подтверждения.')
        return redirect('users:invalid_token')



def invalid_token_view(request):
    return render(request, 'users/invalid_token.html')