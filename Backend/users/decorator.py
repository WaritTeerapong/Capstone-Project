import jwt
import environ

from rest_framework.response import Response
from rest_framework import status

from users.views import home
from users.models import User,Admin


from functools import wraps # python libs to protect the decorator function

def required_login(view_func):
    @wraps(view_func)
    def wrapper_func(request,*args, **kwargs):
        env = environ.Env()
        token = request.COOKIES.get('token')
        if not token:
            return Response(data={'message':'Account unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = jwt.decode(token, env('jwt_secret'), algorithms=['HS256'])
            user = User.objects.get(userID=payload['id']).first()
            
            if user != None:
                request.user = user
            else:
                return Response(data={'message':'This user does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
            
            
        except jwt.ExpiredSignatureError as error:
            return Response(data={'message':str(e) for e in error}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        return view_func(request, *args, **kwargs)
    
    return wrapper_func


# check if user is already login
def is_login(view_func):
    @wraps(view_func)
    def wrapper_func(request,*args, **kwargs):
        token = request.COOKIES.get('token')
        
        if not token :
            return view_func(request, *args, **kwargs)
        
        return Response(data={'message':'User is Authorized'}, status=status.HTTP_200_OK) # redirect to home page if user is already login
    
    return wrapper_func
    
# admin_only
def admin_only(view_func):
    @wraps(view_func)
    def wrapper_func(request,*args, **kwargs):
        # check if this ID exist in admin table
        
        return view_func(request, *args, **kwargs)
    
    return wrapper_func