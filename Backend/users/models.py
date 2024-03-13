from django.db import models
from django.utils import timezone
import items.models as items

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
    
class Request(models.Model):
    requestID = models.AutoField(primary_key=True)
    userID = models.ForeignKey( to = User, on_delete=models.CASCADE)
    placeID = models.ForeignKey( to = items.Place, on_delete=models.CASCADE)
    categoryID = models.ForeignKey( to = items.Category, on_delete=models.CASCADE)
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
        return self.requestDetail