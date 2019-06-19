from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Place

class IndexView(generic.ListView):
  model = Place

class DetailView(generic.DetailView):
  model = Place

class CreateView(generic.edit.CreateView):
  model = Place
  fields = '__all__'

class UpdateView(generic.edit.UpdateView):
  model = Place
  fields = '__all__'

class DeleteView(generic.edit.DeleteView):
  model = Place
  success_url = reverse_lazy('datingmap:index')