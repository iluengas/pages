from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    # “TemplateView already contains all the logic needed
    # to display our template, we just need to specify the template’s name.”
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"