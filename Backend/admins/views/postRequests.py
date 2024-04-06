
from django.http import JsonResponse
from admins.models import PostRequest
from admins.serializers import PostRequestSerializer

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def postRequests_list(request):
    if request.method == 'GET':
        postRequests = PostRequest.objects.all()
        serializer = PostRequestSerializer(postRequests, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def postRequest_by_id(request, id):
    try:
        postRequest = PostRequest.objects.get(pk=id)
    except PostRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostRequestSerializer(postRequest)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostRequestSerializer(postRequest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        postRequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)