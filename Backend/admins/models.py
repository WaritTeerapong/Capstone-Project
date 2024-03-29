from django.db import models
from users.models import Item, Request
from django.utils import timezone

# Create your models here.
class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    Password = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    postID = models.AutoField(primary_key=True, unique=True)
    adminID = models.ForeignKey(to = Admin, on_delete=models.CASCADE)
    itemID = models.ForeignKey(to = Item, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    datePost = models.DateField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.postID
    
class PostRequest(models.Model):
    postID = models.ForeignKey(to = Post, on_delete=models.CASCADE)
    requestID = models.ForeignKey(to = Request, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.requestID