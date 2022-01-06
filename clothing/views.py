from .filter import ProductFilter
from .models import Product, season, gender

from django.views.generic import ListView


class Home(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['seasons'] = season
        context['genders'] = gender

        return context