from .views import NoteRetrive,NoteRetriveAuth
from django.urls import path
from django.conf.urls import include, url
# from fundoo.swagger_view import schema_view

urlpatterns = [

    path("notes", NoteRetrive.as_view(), name="notes"),
    path("notesauth", NoteRetriveAuth.as_view(), name="notes"),
    path('' ,include('djoser.urls')),
    path('' ,include('djoser.urls.authtoken')),
]