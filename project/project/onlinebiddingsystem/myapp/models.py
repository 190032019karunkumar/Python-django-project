from django.db import models

class Bid(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    price = models.IntegerField()
    owner = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    class Meta:  
        db_table = "bid"

class Product(models.Model):
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    owner = models.CharField(max_length=100)
    timer = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    class Meta:
        db_table = "products"

class Test(models.Model):
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pics')
    story = models.CharField(max_length=500)
    class Meta:
        db_table = "test"

class Daily(models.Model):
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    owner = models.CharField(max_length=100)
    timer = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    class Meta:
        db_table = "daily"

class All(models.Model):
    name = models.CharField(max_length=80)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    owner = models.CharField(max_length=100)
    timer = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    class Meta:
        db_table = "all"

class Offer(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    off = models.CharField(max_length=100)
    code = models.CharField(max_length=15)
    expires = models.CharField(max_length=50)
    class Meta:  
        db_table = "offer"