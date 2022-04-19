from django.shortcuts import render
from django.views.generic import TemplateView


class CatalogHomeView(TemplateView):
    template_name = 'catalog/catalog_home.html'