from users.models import Item
from users.serializers import ItemSerializer

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

import cloudinary.uploader
import cloudinary


#-------------------------------------- item
@api_view(['GET', 'POST'])
def items_list(request):
    
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"items":serializer.data}, safe=False)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_by_id(request, id):
    
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response("Item ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # delete item image from cloudinary
        serializer = ItemSerializer(item)
        imgPublicID = serializer.data['image'].split('/')[-1].split('.')[0]
        cloudinary.api.delete_resources(imgPublicID, resource_type="image", type="upload")
        
        # delete item from database
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
