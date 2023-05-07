from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Post-defined urls
    path('', include('Posts.urls')),
    path('auth', include('Users.urls')),
]
