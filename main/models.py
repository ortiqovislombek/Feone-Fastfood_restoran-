from django.db import models

class HeroSlider(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    published=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title
    
class Product(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/products/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,related_name='product', null=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='images/clients/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Order(models.Model):
   
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    payment_method = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.full_name    