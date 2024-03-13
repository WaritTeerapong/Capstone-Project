from django.db import models
from django.utils import timezone
import users.models as users

# from django.apps import apps
# User = apps.get_model('users', 'User')

# Create your models here.

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
    categoryID = models.ForeignKey( to = Category, on_delete=models.CASCADE)
    placeID = models.ForeignKey(to = Place, on_delete=models.CASCADE)
    userID = models.ForeignKey( to = users.User, on_delete=models.CASCADE)
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
    