import hashlib, re
from django.shortcuts import render
from random import SystemRandom, choice
from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from django.views import View
# Create your views here.
EMAIL_REGEX = re.compile(r"/\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b/gi")

def generate_session_token(password=None, salt=None):
    m = hashlib.sha256()
    if password:
        m.update(password.encode('utf-8'))
    else:
        m.update('test'.encode('utf-8'))
    if salt:
        m.update(salt.encode('utf-8'))
    else:
        m.update(b'temp')
    m.digest()
    return m.hexdigest()

@method_decorator(csrf_exempt, name='dispatch')
class LoginPageView(View):
    
    def get(self, request):
        return JsonResponse({'error':'Not a valid request through post'})
    
    
    def post(self, request):
        username = request.POST.get('email', None)
        password = request.POST.get('password', None)
        # print(password)
        # if not EMAIL_REGEX.match(username):
        #     return JsonResponse({'error':'Invalid Email Address'})
        # if len(password) < 8:
        #     return JsonResponse({'error':'Password is less than 8 characters'})
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username) 
            if user.check_password(password):
                usr_dict = user_model.objects.filter(email=username).values().first()
                #usr_dict.pop('password')
                
                if user.session_token != '0':
                    user.session_token = '0'
                    user.save()
                    return JsonResponse({"error": "Session token error"})
                token = generate_session_token()
                user.session_token = token
                user.save()
                login(request, user, 'django.contrib.auth.backends.ModelBackend')
                return JsonResponse({'token': token, 'user':usr_dict})
            else:
                return JsonResponse({"error": "username or password verification failed"})
                
        except user_model.DoesNotExist:
            return JsonResponse({"error": "verification failed"})
            
        

class LogoutView(View):
    def get(self, request, id):
        logout(request)
        user_model = get_user_model()
        try:
            user = user_model.objects.get(pk=id)
            user.session_token = '0'
            user.save()
        except user_model.DoesNotExist:
            return JsonResponse({"error": "No such user ID"})
        return JsonResponse('Success', safe=False)
    

class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        try:
            return []
        except KeyError:
            return []
            
    # def get_permissions(self):
    #     try:
    #         # return permission_classes depending on `action` 
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError: 
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes]
        
        
        
if __name__ == '__main__':
    print(generate_session_token('123123', 'asd'))
    print(len(generate_session_token('123123')))
