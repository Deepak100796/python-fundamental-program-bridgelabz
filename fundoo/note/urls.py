from .views import NoteCreate
from django.urls import path
from django.conf.urls import include, url
# from fundoo.swagger_view import schema_view

urlpatterns = [

    path("notes/", NoteCreate.as_view(), name="notes"),
]