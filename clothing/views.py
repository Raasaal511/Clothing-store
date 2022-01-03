from django.shortcuts import render, get_object_or_404

from .models import Product, season, gender


def home(request) -> render:
    products = Product.objects .all()
    list_gender = get_list_filter(gender)
    list_season = get_list_filter(season)

    context = {
        'products': products,
        'list_gender': list_gender,
        'list_season': list_season,
    }

    return render(request, 'main/home.html', context)


def filter_products(request, season_slug) -> render:
    filter_clothes = Product.objects.filter(season=season_slug)

    return render(request, 'main/filter_product.html', {'filter_clothes': filter_clothes})


def get_list_filter(type_filter) -> list:
    seasons = []
    for i in range(len(type_filter)):
        seasons.append(type_filter[i][1])

    # seasons = ' '.join(seasons)
    return seasons