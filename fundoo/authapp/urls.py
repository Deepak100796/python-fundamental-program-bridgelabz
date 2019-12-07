from django.urls import path,include
from .views import FileView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('' ,include('djoser.urls')),
    path('' ,include('djoser.urls.authtoken')),
    # path('upload/', MyFileView.as_view(), name='upload'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),

    # path('upload/', FileUploadView.as_view())
    # path('upload/',DocumentCreateView)
]
