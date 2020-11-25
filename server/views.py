# For testing google auth
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'