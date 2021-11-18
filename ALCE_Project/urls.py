from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPair, TokenRefreshView
from auth_custom.views.userCreateView import UserCreateView
from auth_custom.views.userDetailView import UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPair),
    path('refresh/', TokenRefreshView),
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view())
]
