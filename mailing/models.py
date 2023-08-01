from django.db import models
from django.forms import ModelForm
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):

    theme = models.CharField(max_length=150, verbose_name='тема сообщения')
    body = models.TextField()

    def __str__(self):
        return f"{self.theme}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):

    TITLE_CHOICES_PERIODICITY = [
        (1, 'Раз в день'),
        (2, 'Раз в неделю',),
        (3, 'Раз в месяц',),
    ]

    TITLE_CHOICES_STATUS = [
        (1, 'Создана'),
        (2, 'Запущена',),
        (3, 'Завершена',),
    ]

    mailing_time = models.DateTimeField(verbose_name="время рассылки", default=timezone.now)
    periodicity = models.PositiveSmallIntegerField(verbose_name="периодичность", choices=TITLE_CHOICES_PERIODICITY, default=1)
    status = models.PositiveSmallIntegerField(verbose_name='статус рассылки', choices=TITLE_CHOICES_STATUS, default=1)
    massage = models.ForeignKey(Message, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.status}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Log(models.Model):

    date_attempt = models.DateTimeField(verbose_name='Дата попытки')
    status = models.CharField(max_length=100, verbose_name='Статус попытки')
    answer = models.CharField(max_length=100, **NULLABLE, verbose_name='ответ сервера')

    def __str__(self):
        return f"{self.status} {self.date_attempt}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


