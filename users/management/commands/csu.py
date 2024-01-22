from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user =User.objects.create(
            email='ilyalew@mail.ru',
            first_name='Admin',
            last_name='Adminov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('645595715abcd')
        user.save()