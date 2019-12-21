from django.shortcuts import render

# Create your views here.

import json

# import requests
# from oauthlib.oauth2 import BackendApplicationClient
from datetime import datetime, timedelta
from functools import wraps
from django.utils import timezone
import django
from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.utils import timezone as tz
from django.shortcuts import get_object_or_404, render
import redis
import pdb
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics,pagination

# from fundoo.settings import PORT, DB, file_handler, TWITTER_PAGE, logging, SOCIAL_AUTH_GITHUB_KEY, \
    # SOCIAL_AUTH_GITHUB_SECRET
# from .documents import NotesDocument
from .serialized import NotesSerializer 
  # ArchiveSerializer
# from lib.amazones3 import AmazoneS3
 # , label_coll_validator_post
from lib.redis import red
# import logging
from .models import Notes, Label
# from pymitter import EventEmitter

# ee = EventEmitter()
# s3 = AmazoneS3()

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticated

# @method_decorator(login_decorator, name='dispatch')
class NoteRetrive(generics.ListAPIView):
    """
        Summary:
        --------
            Note class will let authorized user to create and get notes.
        Methods:
        --------
            get: User will get all the notes.
            post: User will able to create new note.
    """
    queryset = Notes.objects.all()
    serializer = NotesSerializer(queryset, many=True)
    pagination_class = pagination.PageNumberPagination
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
           Summary:
           --------
                All the notes will be fetched for the user.
           Exception:
           ----------
               PageNotAnInteger: object
               EmptyPage: object
           Returns:
           --------
               Html_page: pagination.html    Jinja-arg=['notes']
        """
        
        queryset = self.get_queryset()
        
        serializer= NotesSerializer(queryset,many=True)
        return Response(serializer.data,status=200)

class NoteRetriveAuth(generics.ListAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self,*args, **kwargs):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        qs = Notes.objects.all()
        qs=  qs.filter(User=self.request.user)


    # parser_classes = (FormParser,FileUploadParser)
    # @staticmethod
    # def post(request):
    #     """
    #          Summary:
    #          --------
    #              New note will be create by the User.
    #          Exception:
    #          ----------
    #              KeyError: object
    #          Returns:
    #          --------
    #              response: SMD format of note create message or with error message
    #     """

    #     user = request.user
    #     try:
    #         # data is taken from user
    #         # pdb.set_trace()
    #         data = request.data
    #         if len(data) == 0:
    #             raise KeyError
    #         user = request.user
    #         collaborator_list = []  # empty coll  list is formed where data is input is converted to id
    #         try:
    #             # for loop is used for the getting label input and coll input ids
    #             data["label"] = [Label.objects.filter(user_id=user.id, name=name).values()[0]['id'] for name in
    #                              data["label"]]
    #         except KeyError:
    #             # logger.debug('label was not added by the user %s', user)
    #             pass
    #         try:
    #             collaborator = data['collaborators']
    #             # for loop is used for the getting label input and coll input ids
    #             for email in collaborator:
    #                 email_id = User.objects.filter(email=email)
    #                 user_id = email_id.values()[0]['id']
    #                 collaborator_list.append(user_id)
    #             data['collaborators'] = collaborator_list
    #             print(data['collaborators'])
    #         except KeyError:
    #             # logger.debug('collaborator was not added by the user %s', user)
    #             pass
    #         serializer = NotesSerializer(data=data, partial=True)
    #         if serializer.is_valid():
    #             note_create = serializer.save(user_id=user.id)
    #             response = {'success': True, 'message': "note created", 'data': []}
    #             if serializer.data['is_archive']:
    #                 red.hmset(str(user.id) + "is_archive",
    #                           {note_create.id: str(json.dumps(serializer.data))})  # created note is cached in redis
    #                 # logger.info("note is created for %s with note id as %s", user, note_create.id)
    #                 return HttpResponse(json.dumps(response, indent=2), status=201)
    #             else:
    #                 if serializer.data['reminder']:
    #                     red.hmset("reminder",
    #                               {note_create.id: str(json.dumps({"email": user.email, "user": str(user),
    #                                                                "note_id": note_create.id,
    #                                                                "reminder": serializer.data["reminder"]}))})
    #                 red.hmset(str(user.id) + "note",
    #                           {note_create.id: str(json.dumps(serializer.data))})

    #                 # logger.info("note is created for %s with note data as %s", user, note_create.__repr__())
    #                 return HttpResponse(json.dumps(response, indent=2), status=201)
    #         # logger.error(" %s for  %s", user, serializer.errors)
    #         response = {'success': False, 'message': "note was not created", 'data': []}
    #         return HttpResponse(json.dumps(response, indent=2), status=400)
    #     except KeyError as e:
    #         print(e)
    #         # logger.error("got %s error for creating note as no data was provided for user %s", str(e), user)
    #         response = {'success': False, 'message': "one of the field is empty ", 'data': []}
    #         return Response(response, status=400)
    #     except Exception as e:
    #         print(e)
    #         # logger.error("got %s error for creating note for user %s", str(e), user)
    #         response = {'success': False, 'message': "something went wrong", 'data': []}
    #         return Response(response, status=400)
