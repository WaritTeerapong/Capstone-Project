from django.http import JsonResponse

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

import cloudinary.uploader
import cloudinary

from users.Model import callModel
from users.models import Category

# this is for solved error : PosixPath not found
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


#TODO : save pic to cloud 
#TODO : pass image path to yolov5 model



#-----------------------------------------------------------------------

@api_view(['GET'])
def get_category(req):
    # call model -> predict and get category
    predictions,scores,categories = callModel.predict() #pass image path to yolov5 model
    pred_class = Category.objects.filter(categoryID=categories.item()).first() #.tensor.item() -> number
    
    return JsonResponse({"predictions":predictions.tolist(),"scores":scores.tolist(),"categories":categories.tolist(),"category":pred_class.cateName}) 

    '''if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"items":serializer.data}, safe=False)
    return pass 

@api_view(['GET', 'PUT', 'DELETE'])
def item_by_id(request, id):
    
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response("Item ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
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
        '''

    
    


