from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PrivacyView(TemplateView):
    template_name = 'privacy.html'

class FAQSView(TemplateView):
    template_name = 'faqs.html'

class HOWITWORKSView(TemplateView):
    template_name = 'howitworks.html'

class LandingPageView(TemplateView):
    template_name = 'landing.html'
