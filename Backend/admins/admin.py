from django.contrib import admin
from .models import Admin, Post, PostRequest


# Register your models here.
admin.site.register(Admin)
admin.site.register(Post)
admin.site.register(PostRequest)