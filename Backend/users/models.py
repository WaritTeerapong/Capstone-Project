from django.db import models
from django.utils import timezone


# from django.apps import apps
# Place = apps.get_model('items', 'Place')
# Category = apps.get_model('items', 'Category')


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    Password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    cateName = models.CharField(max_length=100)
    def __str__(self):
        return self.cateName
    
class SubCategory(models.Model):
    subCateID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey( to = Category, on_delete=models.CASCADE)
    subCateName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subCateName
    
class Place(models.Model):
    placeID = models.AutoField(primary_key=True)
    placeCode = models.CharField(max_length=3)
    placeName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.placeName
    
class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(to = Category, on_delete=models.CASCADE)
    placeID = models.ForeignKey(to = Place, on_delete=models.CASCADE)
    userID = models.ForeignKey(to = User, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    itemDetail = models.TextField()
    placeDetail = models.TextField()
    image = models.CharField(max_length=512)
    isFound = models.BooleanField( default=False)
    dateFound = models.DateField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Item, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.itemName

class Request(models.Model):
    requestID = models.AutoField(primary_key=True, unique=True)
    userID = models.ForeignKey( to = User, on_delete=models.CASCADE)
    placeID = models.ForeignKey( to = Place, on_delete=models.CASCADE)
    categoryID = models.ForeignKey( to = Category, on_delete=models.CASCADE)
    placeDetail = models.TextField()
    itemDetail = models.TextField()
    image = models.CharField(max_length=512)
    isApproved = models.BooleanField( default=False)
    dateLost = models.DateField()
    dateRequest = models.DateField( auto_now_add=True)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Request, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.itemDetail