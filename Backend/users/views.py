from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from .models import User,Category,SubCategory,Place,Item,Request
from .serializers import UserSerializer,CategorySerializer,SubCategorySerializer,PlaceSerializer,ItemSerializer,RequestSerializer
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
        #get all user from .model
        users = User.objects.all()   
        #serialize them
        serializer = UserSerializer(users, many=True)
        #return json
        return JsonResponse({"users":serializer.data}, safe=False)
   #POST a new user
    elif request.method == 'POST':
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
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)
    
    #Get a user by id
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    
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
def categories_list(request):

    if request.method == 'GET':
        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)
        return JsonResponse({"category":serializer.data}, safe=False)
    
    #POST a new category
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def category_by_id(request, id):
    
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response("Category ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)
    
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

#-------------------------------------- subcategory
@api_view(['GET', 'POST'])  
def subcategories_list(request):
    
    if request.method == 'GET':
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return JsonResponse({"subcategories":serializer.data}, safe=False)
    
    elif request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def subcategory_by_id(request, id):
    
    try:
        subcategory = SubCategory.objects.get(pk=id)
    except SubCategory.DoesNotExist:
        return Response("SubCategory ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SubCategorySerializer(subcategory)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#-------------------------------------- place
@api_view(['GET', 'POST'])
def places_list(request):
    
    if request.method == 'GET':
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return JsonResponse({"places":serializer.data}, safe=False)
    elif request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def place_by_id(request, id):
    
    try:
        place = Place.objects.get(pk=id)
    except Place.DoesNotExist:
        return Response("Place ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#-------------------------------------- item
@api_view(['GET', 'POST'])
def items_list(request):
    
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse({"items":serializer.data}, safe=False)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def item_by_id(request, id):
    
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response("Item ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#-------------------------------------- request
@api_view(['GET', 'POST'])
def requests_list(request):
    
    if request.method == 'GET':
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return JsonResponse({"requests":serializer.data}, safe=False)
    elif request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def request_by_id(request, id):
    
    try:
        request = Request.objects.get(pk=id)
    except Request.DoesNotExist:
        return Response("Request ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RequestSerializer(request)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RequestSerializer(request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

