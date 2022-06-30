from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    bus_model = models.CharField(max_length=100) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #     return  self.id, self.name, self.color, self.bus_model, self.category