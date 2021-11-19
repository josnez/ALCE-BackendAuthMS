from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'department', 'city', 'adrress', 'adrress_complement', 'postal_code']