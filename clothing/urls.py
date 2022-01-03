from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('filter/<str:season_slug>/', views.filter_products, name='filter'),
]