from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Place
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class IndexView(generic.ListView):
  model = Place

class DetailView(generic.DetailView):
  model = Place

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
  model = Place
  fields = ['name', 'address', 'category']  # '__all__'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
  model = Place
  fields = ['name', 'address', 'category']  # '__all__'

  def dispatch(self, request, *args, **kwargs):
    obj = self.get_object()
    if obj.author != self.request.user:
      raise PermissionDenied('You do not have permission to edit.')
    return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
  model = Place
  success_url = reverse_lazy('datingmap:index')