from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.core.validators import validate_email

import torch.nn as nn


# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])
    tel = models.CharField(max_length=20)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Category(models.Model):
    categoryID = models.IntegerField(primary_key=True)
    cateName = models.CharField(max_length=100)
    def __str__(self):
        return self.cateName
    
class Place(models.Model):
    placeID = models.IntegerField(primary_key=True)
    placeCode = models.CharField(max_length=3)
    placeName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.placeName
    
class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    itemDetail = models.TextField()
    placeDetail = models.TextField()
    image = CloudinaryField('image')
    isFound = models.BooleanField( default=False)
    dateFound = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.itemID:
            
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Item, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.itemName

class Request(models.Model):
    requestID = models.AutoField(primary_key=True, unique=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    placeID = models.ForeignKey(Place, on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    placeDetail = models.TextField()
    itemDetail = models.TextField()
    image = CloudinaryField('image')
    isApproved = models.BooleanField( default=False)
    dateLost = models.DateTimeField()
    dateRequest = models.DateTimeField( auto_now_add=True)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.requestID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Request, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.itemDetail
    
class TempImage(models.Model):
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.image.url
