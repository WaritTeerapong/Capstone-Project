"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path("", views.index),
    
    path("admin/", admin.site.urls),
    
    path('users/', views.users_list),
    path('users/<int:id>', views.user_by_id),
    
    path('categories/', views.categories_list),
    path('categories/<int:id>', views.category_by_id),
    
    path('subcategories/', views.subcategories_list),
    path('subcategories/<int:id>', views.subcategory_by_id),
    
    path('places/', views.places_list),
    path('places/<int:id>', views.place_by_id),
    
    path('items/', views.items_list),
    path('items/<int:id>', views.item_by_id),
    
    path('requests/', views.requests_list),
    path('requests/<int:id>', views.request_by_id),
    
    
]
