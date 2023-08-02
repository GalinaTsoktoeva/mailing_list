from datetime import datetime

import smtplib
import pytz
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail

from client.models import Client
from mailing.forms import MailingForms
from mailing.models import Mailing, Log


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    context = {
        'title': "Контакты"
    }
    return render(request, 'mailing/contact.html', context)


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForms
    permission_required = 'mailing.add_mailing'
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        tz = pytz.timezone('Europe/Moscow')
        clients = [client.email for client in Client.objects.filter(user=self.request.user)]
        new_mailing = form.save()
        #print(new_mailing.massage)
        if new_mailing.mailing_time <= datetime.now(tz):
            mail_subject = new_mailing.massage.body if new_mailing.massage is not None else 'Рассылка'
            message = new_mailing.massage.theme if new_mailing.massage is not None else 'Вам назначена рассылка'
            try:
                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, clients)
                log = Log.objects.create(date_attempt=datetime.now(tz), status='Успешно', answer='200', mailing=new_mailing)
                log.save()
            except smtplib.SMTPException as err:
                log = Log.objects.create(date_attempt=datetime.now(tz), status='Ошибка', answer=err, mailing=new_mailing)
                log.save()
                raise err
            except Exception as err:
                log = Log.objects.create(date_attempt=datetime.now(tz), status='Ошибка', answer=err, mailing=new_mailing)
                log.save()
                raise err
            new_mailing.status = 3
            new_mailing.save()

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForms
    permission_required = 'mailing.change_mailing'
    success_url = reverse_lazy('mailing:list')


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'mailing.delete_mailing'
    success_url = reverse_lazy('mailing:list')





