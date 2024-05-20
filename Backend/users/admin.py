from django.contrib import admin
from .models import User, Category, SubCategory, Place, Item, Request

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Place)
admin.site.register(Item)
admin.site.register(Request)