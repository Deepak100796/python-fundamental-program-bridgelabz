from .views import NoteRetrive,CreateNote
from django.urls import path
from django.conf.urls import include, url
# from fundoo.swagger_view import schema_view

urlpatterns = [

    path("notes", NoteRetrive.as_view(), name="notes"),
    path("createnote", CreateNote.as_view(), name="notes"),
    # url(r'^/users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list')
    path('' ,include('djoser.urls')),
    path('' ,include('djoser.urls.authtoken')),
]