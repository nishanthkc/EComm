from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def get_file_path(request, filename):
    original_filename = filename
    now = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (now, original_filename)
    return os.path.join('uploads/', filename)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=trending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_image_1 = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_image_2 = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_image_3 = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_image_4= models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_image_5 = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    product_desciption = models.TextField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    product_status = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    product_trending = models.BooleanField(default=False, help_text='0=default, 1=trending')
    created_at = models.DateTimeField(auto_now_add=True)
    filter_tags = models.CharField(max_length=100, null=False, blank=False)
    
    

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)