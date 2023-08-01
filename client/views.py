from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from client.forms import ClientForms
from client.models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('client:list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForms
    success_url = reverse_lazy('client:list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')