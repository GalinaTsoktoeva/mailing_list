from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail

from client.models import Client
from mailing.forms import MailingForms
from mailing.models import Mailing


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MailingDetailView(DetailView):
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


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForms
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        clients = [client.email for client in Client.objects.all()]
        new_mailing = form.save()
        mail_subject = 'Супер предложение'
        message = 'Рассылка спецпредложений персонально для вас!'
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, clients)
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForms
    success_url = reverse_lazy('mailing:list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list')


