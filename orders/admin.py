from django.contrib import admin

# Register your models here.
from .models import Pizza,Sub,Topping,Pasta,Salad,DinnerPlate
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Topping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlate)