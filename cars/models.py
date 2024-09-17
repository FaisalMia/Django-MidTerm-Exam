from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CarBrand(models.Model):
    brand_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    
    def __str__(self):
        return self.brand_name
    
class CarModel(models.Model):
    car_name = models.CharField(max_length=200)
    car_price = models.IntegerField()
    car_model = models.ForeignKey('CarBrand', related_name='brand', on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='uploads/',null=True,blank=True)
    car_quantity = models.IntegerField(null=True,blank=True)
    buyers = models.ManyToManyField(User, related_name='purchased_cars', blank=True)
    
    def __str__(self):
        return self.car_name
    
class Comment(models.Model):
    carModel = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created_one = models.DateTimeField(auto_now_add=True)
    
    

