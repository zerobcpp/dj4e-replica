from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only':True}}
        fields = ['name', 'email', 'password', 'gender', 
                  'is_active', 'is_staff', 'is_superuser' ]
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        obj = self.Meta.model(**validated_data)
        
        if password:
            obj.set_password(password)
        obj.save()
        return obj
    
    def update(self, id, validated_data):
        for k, v in validated_data.items():
            if k == 'password':
                id.set_password(v)
            else:
                setattr(id, k, v)
        id.save()
        return id
            