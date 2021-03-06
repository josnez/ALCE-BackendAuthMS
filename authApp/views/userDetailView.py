from rest_framework                     import generics

from authApp.models.user                import User
from authApp.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def get(seft, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserUpdateView(generics.UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def update(seft, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def delete(seft, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
