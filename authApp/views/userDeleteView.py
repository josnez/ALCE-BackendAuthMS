from rest_framework                     import generics
from authApp.models.user                import User
from authApp.serializers.userSerializer import UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def delete(seft, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
