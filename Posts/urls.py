from django.urls import path    
from . import views


urlpatterns = [
    path('',views.index, name="post_home" ),
    path('about/',views.about, name="post_about" ),
    path('services/',views.services, name="post_services" ),
    path('create_post/',views.create_post, name="create_post" ),
]
