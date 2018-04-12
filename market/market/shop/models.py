from django.db import models
from django.urls import reverse
 
class Product(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 5000, blank = True)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name='categories')
    def __str__(self): 
        return(self.title)
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Category(models.Model): 
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 5000, blank = True)
    def __str__(self):
        return(self.title)

class Order(models.Model):
    product = models.ForeignKey('Product', on_delete='CASCADE')
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    def __str__(self):
        return(self.title)

class User(models.Model):
    customer_login = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=30)
    customer_password = models.CharField(max_length=15)
    def __str__(self):
        return(self.title)