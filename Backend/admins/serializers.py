from rest_framework import serializers
from .models import PostRequest, Post, Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRequest
        fields = '__all__'
