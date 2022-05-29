from fnmatch import fnmatchcase
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

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, null=False)
    lname = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.CharField(max_length=100, null=False)
    total_amount = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=100, null=False)
    payment_id = models.CharField(max_length=100, null=True)
    orders_status_options = (
        ('Pending','Pending'),
        ('Out for Shipping','Out for Shipping'),
        ('Shipped','Shipped'),
    )
    status = models.CharField(max_length=100,choices=orders_status_options ,default='Pending')
    tracking_number = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_number)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} _____ {} _____ {}'.format(self.id, self.order, self.order.created_at)