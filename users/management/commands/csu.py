from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='galina-tsoktoeva@mail.ru',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()

        my_group = Group.objects.create(name='manager_mailing')
        my_group.user_set.add(user)
