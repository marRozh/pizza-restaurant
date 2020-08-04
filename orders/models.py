from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=30)
    item_category = models.CharField(max_length=30)
    item_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.item_name} {self.item_price}'

class Size(models.Model):
    size_name = models.CharField(max_length=30)
    size_category = models.CharField(max_length=30)
    size_small_price = models.DecimalField(max_digits=5, decimal_places=2)
    size_large_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.size_name} Small: {self.size_small_price} Large: {self.size_large_price}'

class Topping(models.Model):
    topping_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.topping_name}'

class Subtopping(models.Model):
    sub_topping_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.sub_topping_name}'

class Order(models.Model):
    order_date = models.DateField()
    order_time = models.TimeField()
    user = models.CharField(max_length=50)
    item_name = models.CharField(max_length=30)
    item_category = models.CharField(max_length=30)
    item_size = models.CharField(max_length=30, blank=True)
    item_toppings_num = models.IntegerField(default=0, blank=True)
    item_toppings_list = models.CharField(max_length=100, blank=True)
    item_total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.order_date} {self.order_time}: (User ID: {self.user}) Item: {self.item_name} Category: {self.item_category} Size: {self.item_size} Toppings: {self.item_toppings_num} ({self.item_toppings_list}) Total Price: {self.item_total_price}'

class Confirmed(models.Model):
    order_number = models.IntegerField(default=0, blank=True)
    order_date = models.DateField()
    order_time = models.TimeField()
    user = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, blank=True)
    item_name = models.CharField(max_length=30)
    item_category = models.CharField(max_length=30)
    item_size = models.CharField(max_length=30, blank=True)
    item_toppings_num = models.IntegerField(default=0, blank=True)
    item_toppings_list = models.CharField(max_length=100, blank=True)
    item_total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.order_date} {self.order_time}: (User ID: {self.user}) Item: {self.item_name} Category: {self.item_category} Size: {self.item_size} Toppings: {self.item_toppings_num} ({self.item_toppings_list}) Total Price: {self.item_total_price}'

class Complete(models.Model):
    order_number = models.IntegerField(default=0, blank=True)
    order_date = models.DateField()
    order_time = models.TimeField()
    user = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, blank=True)
    item_name = models.CharField(max_length=30)
    item_category = models.CharField(max_length=30)
    item_size = models.CharField(max_length=30, blank=True)
    item_toppings_num = models.IntegerField(default=0, blank=True)
    item_toppings_list = models.CharField(max_length=100, blank=True)
    item_total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.order_date} {self.order_time}: (User ID: {self.user}) Item: {self.item_name} Category: {self.item_category} Size: {self.item_size} Toppings: {self.item_toppings_num} ({self.item_toppings_list}) Total Price: {self.item_total_price}'