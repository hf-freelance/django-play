from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=200)
    def __str__(self):
        return self.label

class Item(models.Model):
    name = models.CharField(max_length=400)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    