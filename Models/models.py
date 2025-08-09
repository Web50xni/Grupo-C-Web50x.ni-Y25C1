from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    class Meta:
        db_table = "country_bottles"

    def __str__(self):
        return self.country_name


class Region(models.Model):
    region_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="regions")

    class Meta:
        db_table = "region"

    def __str__(self):
        return self.region_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name


class Producer(models.Model):
    producer_name = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="producers")

    class Meta:
        db_table = "producer"

    def __str__(self):
        return self.producer_name


class Bottle(models.Model):
    full_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="bottles")
    label = models.TextField(null=True, blank=True)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name="bottles")
    year_produced = models.IntegerField()
    picture = models.TextField(null=True, blank=True)
    alcohol_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "bottle_bottles"

    def __str__(self):
        return self.full_name

