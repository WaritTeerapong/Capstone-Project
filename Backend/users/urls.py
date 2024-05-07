from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.index),
    
    path('sign-up', views.signup),
    path('log-in', views.login),
    path('log-out', views.logout),
    
    path('search-by-photo', views.get_category),
    
    path('users', views.users_list),
    path('users/<int:id>', views.user_by_id),
    
    path('categories', views.categories_list),
    path('categories/<int:id>', views.category_by_id),
    
    path('places', views.places_list),
    path('places/<int:id>', views.place_by_id),
    
    path('items', views.items_list),
    path('items/<int:id>', views.item_by_id),
    
    path('requests', views.userRequests_list),
    path('requests/<int:id>', views.userRequest_by_id),
    
]
