from rest_framework import serializers
from .models import User,Category,Place,Item,Request

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class UserRequestSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Request
        fields = '__all__'  
        
class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class LogInSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'