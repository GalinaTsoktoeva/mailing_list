# Generated by Django 4.2.3 on 2023-08-02 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0005_log_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.AddField(
            model_name='mailing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
