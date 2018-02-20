"""Home App."""
# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.

# old view function for home page
# def home(request):
#     """Home Page."""
#     template = 'home/home.html'
#     context = {'user': 'Dear', }
#     # return HttpResponse("Hello")
#    return render(request, template, context)

class Home(TemplateView):
    """Home Page Class Based View."""

    template_name = 'home/home.html'
    context = {'title': 'Toran Sahu'}
