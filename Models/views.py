from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Country, Region, Category, Producer, Bottle
from .forms import CountryForm, RegionForm, CategoryForm, ProducerForm, BottleForm


# --- Country ---
class CountryListView(ListView):
    model = Country
    template_name = "country/list.html"


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = "form.html"
    success_url = reverse_lazy("country_list")


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = "form.html"
    success_url = reverse_lazy("country_list")


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("country_list")


# --- Region ---
class RegionListView(ListView):
    model = Region
    template_name = "region/list.html"


class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = "form.html"
    success_url = reverse_lazy("region_list")


class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = "form.html"
    success_url = reverse_lazy("region_list")


class RegionDeleteView(DeleteView):
    model = Region
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("region_list")


# --- Category ---
class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "form.html"
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "form.html"
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("category_list")


# --- Producer ---
class ProducerListView(ListView):
    model = Producer
    template_name = "producer/list.html"


class ProducerCreateView(CreateView):
    model = Producer
    form_class = ProducerForm
    template_name = "form.html"
    success_url = reverse_lazy("producer_list")


class ProducerUpdateView(UpdateView):
    model = Producer
    form_class = ProducerForm
    template_name = "form.html"
    success_url = reverse_lazy("producer_list")


class ProducerDeleteView(DeleteView):
    model = Producer
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("producer_list")


# --- Bottle ---
class BottleListView(ListView):
    model = Bottle
    template_name = "bottle/list.html"


class BottleCreateView(CreateView):
    model = Bottle
    form_class = BottleForm
    template_name = "form.html"
    success_url = reverse_lazy("bottle_list")


class BottleUpdateView(UpdateView):
    model = Bottle
    form_class = BottleForm
    template_name = "form.html"
    success_url = reverse_lazy("bottle_list")


class BottleDeleteView(DeleteView):
    model = Bottle
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("bottle_list")


# Manda un patito en el grupo si llegaste hasta aquí  🦆
