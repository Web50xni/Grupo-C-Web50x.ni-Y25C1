from django.urls import path
from .views import (
    CountryListView, CountryCreateView, CountryUpdateView, CountryDeleteView,
    RegionListView, RegionCreateView, RegionUpdateView, RegionDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    ProducerListView, ProducerCreateView, ProducerUpdateView, ProducerDeleteView,
    BottleListView, BottleCreateView, BottleUpdateView, BottleDeleteView
)

urlpatterns = [
    # Country
    path("", CountryListView.as_view(), name="main"),
    path("countries/", CountryListView.as_view(), name="country_list"),
    path("countries/add/", CountryCreateView.as_view(), name="country_add"),
    path("countries/<int:pk>/edit/", CountryUpdateView.as_view(), name="country_edit"),
    path("countries/<int:pk>/delete/", CountryDeleteView.as_view(), name="country_delete"),

    # Region
    path("regions/", RegionListView.as_view(), name="region_list"),
    path("regions/add/", RegionCreateView.as_view(), name="region_add"),
    path("regions/<int:pk>/edit/", RegionUpdateView.as_view(), name="region_edit"),
    path("regions/<int:pk>/delete/", RegionDeleteView.as_view(), name="region_delete"),

    # Category
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/add/", CategoryCreateView.as_view(), name="category_add"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),

    # Producer
    path("producers/", ProducerListView.as_view(), name="producer_list"),
    path("producers/add/", ProducerCreateView.as_view(), name="producer_add"),
    path("producers/<int:pk>/edit/", ProducerUpdateView.as_view(), name="producer_edit"),
    path("producers/<int:pk>/delete/", ProducerDeleteView.as_view(), name="producer_delete"),

    # Bottle
    path("bottles/", BottleListView.as_view(), name="bottle_list"),
    path("bottles/add/", BottleCreateView.as_view(), name="bottle_add"),
    path("bottles/<int:pk>/edit/", BottleUpdateView.as_view(), name="bottle_edit"),
    path("bottles/<int:pk>/delete/", BottleDeleteView.as_view(), name="bottle_delete"),
]
