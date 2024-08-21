from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):
    car_name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    
    description=models.TextField()
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='car/media/uploads',blank='True',null='True')
    quantity = models.IntegerField(default=0) 

    def __str__(self):
        return self.car_name
    

      
    
class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  f"Comments By {self.name}"



        



