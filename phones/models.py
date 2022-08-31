from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=300)
    release_date = models.CharField(max_length=100)
    lte_exists = models.CharField(max_length=10) #true false надо сделать
    slug = models.SlugField()
