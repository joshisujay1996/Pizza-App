from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):

    # Pizza Types which is either Regular or Sicilian
    Pizza_Type = (
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )

    # Pizza size either Small or Large
    Pizza_Size = (
        ('SMALL', 'Small'),
        ('LARGE', 'Large'),
    )

    # number of toppings
    TOPPING_CHOICE = (
        ('CHEESE', 'Cheese'),
        ('ONE_TOPPING', 'One'),
        ('TWO_TOPPING', 'Two'),
        ('THREE_TOPPING', 'Three'),
        ('SPECIAL_FIVE_TOPPING', 'FiveSpl'),
    )

    pizzaType = models.CharField(max_length = 1, choices = Pizza_Type)
    size = models.CharField(max_length = 20, choices = Pizza_Size)
    NumbOfTp = models.CharField(max_length = 20, choices = TOPPING_CHOICE)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return f"The pizza type chosen is {self.pizzaType}, its size is  {self.size}, the topping count is  {self.NumbOfTp} and the price is {self.price}"

class Sub(models.Model):

    # Size of sub: Small or Large
    Sub_Size = (
        ('SMALL', 'Small'),
        ('LARGE', 'Large'),
    )

    # Extra Cheese ?
    CHEESE_CHOICE = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    Sub_Type=(
        ('C','CHEESE'),
        ('I','Italian'),
        ('HC','Ham and cheese'),
        ('MB','MEATBALL'),
        ('T','TUNA'),
        ('TK','turkey'),
        ('CP','chicken parm'),
        ('EP','eggplan parm'),
        ('S','steak'),
        ('SC','steak and cheese'),
        ('SPO','sausage,pepper and onions'),
        ('HB','Ham burger'),
        ('CB','cheese burger'),
        ('FC','fried chicken'),
        ('V','Veggie'),

    )
    sub_type = models.CharField(max_length=20, choices=Sub_Type)
    size = models.CharField(max_length=20, choices=Sub_Size)
    extra_cheese = models.CharField(max_length=10, choices=CHEESE_CHOICE)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"The sub choosen is  {self.sub_type}, its size is {self.size} with  Extra Cheese {self.extra_cheese} and price is {self.price}"

        #Check
class Topping(models.Model):
    topping = models.CharField(max_length=64)
    pizza = models.ManyToManyField(Pizza, blank=True, related_name='toppings')
    sub = models.ManyToManyField(Sub, blank=True, related_name='toppings')


    def __str__(self):
        return f"Topping: {self.topping}"

class Pasta(models.Model):

    # Pasta Types
    PASTA_TYPES = (
        ('ZITI_MOZZERELLA', 'Baked Ziti w/ Mozerella'),
        ('ZITI_MEATBALL', 'Baked Ziti w/ Meatballs'),
        ('ZITI_CHICKEN', 'Baked Ziti w/ Chicken')
    )

    pasta_type = models.CharField(max_length = 20, choices=PASTA_TYPES)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Pasta Type is {self.pasta_type} and Price is {self.price}"

class Salad(models.Model):

    # Salad Choices
    SALAD_CHOICES = (
        ('GARDEN', 'Garden Salad'),
        ('GREEK', 'Greek Salad'),
        ('ANTIPASTO', 'Antipasto'),
        ('TUNA', 'Salad w/ Tuna')
    )

    salad_type = models.CharField(max_length = 20, choices=SALAD_CHOICES)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Salad Type: {self.salad_type}, Price: {self.price}"

class DinnerPlate(models.Model):
    DINNER_CHOICE=(
        ('GARDEN', 'Garden Salad'),
        ('GREEK', 'Greek Salad'),
        ('ANTIPASTO', 'Antipasto'),
        ('BAKED','baked Ziti'),
        ('MEATBALL','meatball parm'),
        ('CHICKEN','chicken parm')

    )
    # Size - Small or Large
    SIZE_CHOICES = (
        ('SMALL', 'Small'),
        ('LARGE', 'Large')
    )

    dinner = models.CharField(max_length=20, choices=DINNER_CHOICE)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Dinner plate chosen is {self.dinner} its Size is {self.size} and Price is {self.price}"
