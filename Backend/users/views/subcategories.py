from django.http import JsonResponse
from users.models import SubCategory
from users.serializers import SubCategorySerializer

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

