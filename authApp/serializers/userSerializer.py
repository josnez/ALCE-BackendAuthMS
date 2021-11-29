from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email', 'department', 'city', 'address', 'address_complement', 'postal_code', 'num_changed_books']

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id'                   : user.id,
            'name'                 : user.name,
            'last_name'            : user.last_name,
            'email'                : user.email,
            'department'           : user.department,
            'city'                 : user.city,
            'address'              : user.address,
            'adrress_complement'   : user.address_complement,
            'postal_code'          : user.postal_code,
            'num_changed_books'    : user.num_changed_books
        }