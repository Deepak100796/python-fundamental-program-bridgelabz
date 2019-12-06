from django.urls import path,include
from .views import image_upload
urlpatterns = [
   
    path('' ,include('djoser.urls')),
    path('' ,include('djoser.urls.authtoken')),
    path('image_upload/',image_upload, name='image_uploads')
]
