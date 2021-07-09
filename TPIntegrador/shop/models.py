from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seccion(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.descripcion}"

class Products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="clasificacion_seccion")
    description = models.TextField()
    image = models.CharField(max_length=300) 

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
