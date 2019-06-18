from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Place

class IndexView(generic.ListView):
  model = Place
  