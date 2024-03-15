from django.db import models

# Create your models here.
class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    Password = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name