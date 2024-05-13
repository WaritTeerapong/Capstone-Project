from users.models import Item
from users.serializers import ItemSerializer ,ItemCategorySerializer

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

import cloudinary.uploader
import cloudinary

#-------------------------------------- item
@api_view(['GET', 'POST'])
def items_list(req):
    
    if req.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"items":serializer.data})
    elif req.method == 'POST':
        serializer = ItemSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_req)

@api_view(['GET', 'PUT', 'DELETE'])
def item_by_id(req, id):
    
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response("Item ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif req.method == 'PUT':
        serializer = ItemSerializer(item, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_req)
    
    elif req.method == 'DELETE':
        # delete item image from cloudinary
        serializer = ItemSerializer(item)
        imgPublicID = serializer.data['image'].split('/')[-1].split('.')[0]
        cloudinary.api.delete_resources(imgPublicID, resource_type="image", type="upload")
        
        # delete item from database
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def items_by_category(req,cate_id):
    try:
        items = Item.objects.filter(categoryID=cate_id)
    except Item.DoesNotExist:
        return Response("None of the items found in the Category", status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        serializer = ItemCategorySerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


#TODO : save pic to cloud 

from users.Model import callModel
from users.form import TempImageForm

@api_view(['GET','POST'])
def items_by_img(req,img_path):
    
    if req.method == 'POST':
        
        #get img file through form and save it to temp model
        form = TempImageForm(data=req.POST, files=req.FILES)
        if form.is_valid():
            # upload image to cloudinary
            cloudinary.uploader.upload(req.FILES['file'])
            img_path = cloudinary.utils.cloudinary_url(req.FILES['file'].name)[0]
            '''
            #another way to upload image to cloudinary
            
            cloudinary.uploader.upload("http://www.example.com/image.jpg", public_id = 'sample_remote')
            cloudinary.utils.cloudinary_url("sample_remote.jpg")

            # http://res.cloudinary.com/demo/image/upload/sample_remote.jpg'''
        else: 
            return Response("Invalid Form", status=status.HTTP_400_BAD_req)
        
        try:
            # call model -> predict and get category
            categories = callModel.predict(img_path) #pass image path to yolov5 model
            #pred_class = Category.objects.filter(categoryID=categories.item()).first() #.tensor.item() -> number
            items_cate = Item.objects.filter(categoryID=categories.item())
            #delete temp image from cloudinary
            imgPublicID = 'temp_img'
            cloudinary.api.delete_resources(imgPublicID, resource_type="image", type="upload")
        except Item.DoesNotExist:
            return Response("None of the items found in the Category", status=status.HTTP_404_NOT_FOUND)

        serializer = ItemCategorySerializer(items_cate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response({"predictions":predictions.tolist(),"scores":scores.tolist(),"categories":categories.tolist(),"category":pred_class.cateName}) 
        
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

