from rest_framework                     import generics
from authApp.models.user                import User
from authApp.serializers.userSerializer import UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def update(seft, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)