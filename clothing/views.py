from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product, season, gender

from django.views.generic import View, ListView


class Home(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['seasons'] = season
        context['genders'] = gender

        return context


def filter_products(request, season_slug) -> render:
    filter_clothes = Product.objects.filter(season=season_slug)

    return render(request, 'main/filter.html', {'filter_clothes': filter_clothes})
