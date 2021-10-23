from django.contrib import admin
from .models import Size, Topping, Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'type']

admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Pizza, PizzaAdmin)
