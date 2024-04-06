
from django.http import JsonResponse
from users.models import Request
from users.serializers import UserRequestSerializer

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

import cloudinary.uploader
import cloudinary



#-------------------------------------- request
@api_view(['GET', 'POST'])
def userRequests_list(request):
    
    if request.method == 'GET':
        user_requests = Request.objects.all() # this Request is model request not the "request from clients"
        serializer = UserRequestSerializer(user_requests, many=True)
        return JsonResponse({"requests":serializer.data}, safe=False)
    elif request.method == 'POST':
        serializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def userRequest_by_id(request, id):
    
    try:
        user_requests = Request.objects.get(pk=id)
    except Request.DoesNotExist:
        return Response("Request ID not found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserRequestSerializer(user_requests)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserRequestSerializer(user_requests, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # delete request image from cloudinary
        serializer = UserRequestSerializer(user_requests)
        imgPublicID = serializer.data['image'].split('/')[-1].split('.')[0]
        cloudinary.api.delete_resources(imgPublicID, resource_type="image", type="upload")
        
        # delete item from database
        user_requests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

