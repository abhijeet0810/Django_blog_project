from django.shortcuts import render
from django.http import HttpResponse
# We are using Totorial here so it needs to import
from .models import Tutorial
from django.views.generic.list import ListView
# Create your views here.
# This is the display of the website or just viwes

# def homepage(request):
#     return HttpResponse("<strong>Hello, world.</strong>You're at the Homepage.")

# Here we are changing the homepage function to render a template from template folder
# render parameters:


# def homepage(request):
#     return render(request = request,
#                   template_name='main/home.html',
#                   context = {"tutorials":Tutorial.objects.all})

class TutorialListView(ListView):
    model = Tutorial
    template_name = 'main/home.html'
