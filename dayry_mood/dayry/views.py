from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dyary
from django.urls import reverse_lazy

class DyaryList(ListView):
	model = Dyary

class DyaryDetail(DetailView):
	model = Dyary

class DyaryCreate(CreateView):
	model = Dyary 
	fields = ['text', 'scale', 'time_now']
	success_url = reverse_lazy('dyary_update')


class DyaryUpdate(UpdateView):
	model = Dyary
	fields = ['text', 'scale', 'time_now']
	success_url = reverse_lazy('dyary_update')

class DyaryDelete(DeleteView):
	model = Dyary
	success_url = reverse_lazy('dyary_update')
