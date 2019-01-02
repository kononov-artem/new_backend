from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('word.urls')),
    path(r'api/v1/', include('api.urls')),
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'auth/', include('djoser.urls.jwt')),
]
