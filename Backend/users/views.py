from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from .models import User,Category,SubCategory,Place,Item
from .serializers import UserSerializer,CategorySerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html')

#-------------------------------------- users
@api_view(['GET', 'POST'])
def users_list(request):
    #GET all users
    if request.method == 'GET':
        #get all username
        users = User.objects.all()   
        #serialize them
        serializer = UserSerializer(users, many=True)
        #return json
        return JsonResponse({"users":serializer.data}, safe=False)
   #POST a new user
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def user_by_id(request, id):
    
    #find user by id
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response("User ID:",id,"not found", status=status.HTTP_404_NOT_FOUND)
    
    #Get a user by id
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    #Update a user by id
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Delete a user by id
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
#-------------------------------------- catergory
@api_view(['GET', 'POST'])
def category_list(request):

    if request.method == 'GET':
        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)
        return JsonResponse({"category":serializer.data}, safe=False)
    #POST a new category
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view([['GET', 'PUT', 'DELETE']])
def category_by_id(request, id):
    
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response("Category ID:",id,"not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)