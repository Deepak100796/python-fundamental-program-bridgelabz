from .views import NoteRetrive
from django.urls import path
from django.conf.urls import include, url
# from fundoo.swagger_view import schema_view

urlpatterns = [

    path("notes", NoteRetrive.as_view(), name="notes"),
]