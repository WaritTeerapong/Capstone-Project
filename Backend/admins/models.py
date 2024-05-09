from django.db import models
from users.models import Item, Request
from django.utils import timezone
from django.core.validators import validate_email

# Create your models here.
class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])
    tel = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    postID = models.AutoField(primary_key=True, unique=True)
    adminID = models.ForeignKey(Admin, on_delete=models.CASCADE)
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    datePost = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.postID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.postID)
    
class PostRequest(models.Model):
    postID = models.ForeignKey(to = Post, on_delete=models.CASCADE)
    requestID = models.ForeignKey(to = Request, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.requestID