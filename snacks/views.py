from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack


# Create your views here.

class Home(TemplateView):
    template_name = 'Home.html'

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snacks'
class SnacksDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack