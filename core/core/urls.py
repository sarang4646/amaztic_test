from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('backend.urls')),
    path('api/', include('backend.api.urls')),
    path('users/', include('userapp.urls')),
]
