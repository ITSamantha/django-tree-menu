from django.db import connection
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import Menu, MenuItem


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.get(slug=context['menu']) if 'menu' in context else Menu.objects.first()
        context['item'] = context['item'] if 'item' in context else 0
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().get(request, *args, **kwargs)

        # Check the number of database queries executed for debugging purposes
        print("Number of database queries: ", len(connection.queries))

        return response
