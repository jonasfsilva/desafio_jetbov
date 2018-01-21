from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    # url_field_name = '_url_'
    
    class Meta:
        model  = User    
        fields = (
            # '_url_',
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
        )