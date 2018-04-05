from django.db import models
 
class Product(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 5000, blank = True)
    category = models.ForeignKey('Category', on_delete = 'CASCADE', null = True, related_name = 'products')
    def __str__(self): 
        return(self.title)


class Category(models.Model): 
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 5000, blank = True)
    product = models.ForeignKey('Product', on_delete = 'CASCADE', null = True, related_name = 'categories')
    def __str__(self):
        return(self.title)

# Create your models here.
