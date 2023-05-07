from django.urls import path    
from . import views


urlpatterns = [
    path('',views.index, name="post_home" ),
    path('about/',views.about, name="post_about" ),
    path('services/',views.services, name="post_services" ),
    path('create_post/',views.create_post, name="create_post" ),
    path('post/<int:post_id>',views.post_detail, name="post_detail" ),
    path('post/update/<int:post_id>',views.update_post, name="update_post" ),
]
