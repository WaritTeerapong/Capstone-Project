from . import views
from django.urls import path

urlpatterns = [
        
    path('posts', views.posts_list),
    path('posts/<int:id>', views.post_by_id),
    
    path('postrequests', views.postRequests_list),
    path('postrequests/<int:id>', views.postRequest_by_id),
]