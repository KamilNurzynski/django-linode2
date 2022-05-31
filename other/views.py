from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView, ListView
from other.forms import ContactForm

# Create your views here.


def simple_view(request):
    return HttpResponse("Cześć Kamil")


class ThankYouView(TemplateView):
    template_name = 'other/thank_you.html'


class HomeView(TemplateView):
    template_name = 'other/home.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'other/contact.html'
