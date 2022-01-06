import django_filters as filters

from clothing.models import Product, gender, season


class ProductFilter(filters.FilterSet):
    price = filters.NumberFilter()
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')

    filter_season = filters.ChoiceFilter(label='filter season', choices=season, method='filter_by_choice')
    filter_gender = filters.ChoiceFilter(label='filter season', choices=gender, method='filter_by_choice')

    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            'season': [],
            'gender': [],
        }

    def filter_by_choice(self, queryset, name, value):
        for se in season:

            if value in se:
                filter_clothes = Product.objects.filter(season=value)
                return filter_clothes

            else:
                filter_clothes = Product.objects.filter(gender=value)
                return filter_clothes

# icontains  это фильтрация более подходяшая в Queryset(запросу)