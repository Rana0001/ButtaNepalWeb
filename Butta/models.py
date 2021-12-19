
from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True)
    customer_first = models.CharField(max_length=25, blank=True)
    customer_last = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    customer_picture = models.FileField(
        upload_to="profile", default="picture.jpg", blank=True
    )
    is_login = models.BooleanField(default=False)
    review = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "customer_tbl"


class Product(models.Model):
    product_id = models.AutoField(auto_created=True, primary_key=True)
    product_name = models.CharField(max_length=50, blank=True)
    product_price = models.CharField(max_length=10, blank=True)
    product_image = models.FileField(
        upload_to="product", default="product.jpg", blank=True
    )

    class Meta:
        db_table = "product_tbl"


class Contact_us(models.Model):
    visitor_id = models.AutoField(auto_created=True, primary_key=True)
    visitor_name = models.CharField(max_length=100, blank=True)
    visitor_subject = models.CharField(max_length=100, blank=True)
    visitor_message = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "contact_tbl"


class Order(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True)
    fullname = models.CharField(max_length=25, default="customer", blank=True)
    country_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    butta = models.FileField(upload_to="butta", default="butta.jpg", blank=True)
    payment_method = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50,blank=True)

    class Meta:
        db_table = "order_tbl"
