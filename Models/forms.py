from django import forms
from .models import Country, Region, Category, Producer, Bottle


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["country_name"]


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["region_name", "country"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name"]


class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ["producer_name", "details", "region"]


class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = [
            "full_name", "category", "label", "volume", "producer",
            "year_produced", "picture", "alcohol_percentage", "current_price"
        ]
