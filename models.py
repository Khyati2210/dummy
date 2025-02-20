from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    # def __str__(self):
    #     return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email

class userregister(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    add=models.TextField()
    mob=models.CharField(max_length=10,default="")
    
    def __str__(self):
        return self.email

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image=models.ImageField()
    def __str__(self):
        return self.name

class ScrapType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='scrap_types')
    name = models.CharField(max_length=255)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
   

    
class Pickup(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking to the User model for user details
    scrap_type = models.CharField(max_length=100)
    weight = models.FloatField()
    total_price = models.FloatField()
    status = models.CharField(max_length=50, default='Pending')  # Can be 'Pending', 'Completed', etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Compost(models.Model):
    name = models.CharField(max_length=255)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name