from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from .models import Place


# Base View for Home
class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "base.html")


# Base View for Documentation
class DocumentationView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "documentation.html")


# Base View for ReadMe
class ReadMeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "read-me.html")


# Base View for Bootstrap
class BootstrapView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "bootstrap.html")


# Bootstrap Using Class Based View

class PlaceList(ListView):
    model = Place


class PlaceCreate(CreateView):
    model = Place
    fields = ['name', 'slug', 'city']
    success_url = '/place-list'


class PlaceDetail(DetailView):
    model = Place


class PlaceUpdate(UpdateView):
    model = Place
    fields = ['name', 'slug', 'city']
    success_url = '/place-list'


class PlaceDelete(DeleteView):
    model = Place
    success_url = '/place-list'

# TODO: Bootstrap Using Generics Views
