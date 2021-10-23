from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    type1 = 'square'
    type2 = 'regular'

    TYPE_CHOICES = (
        (type1, 'Square'),
        (type2, 'Regular')
    )

    name = models.CharField(max_length=50, unique=True, blank=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=False)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, blank=False, default='Regular')
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return self.name
