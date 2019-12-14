from django.shortcuts import render
# for aws import 
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import User
from . models import User

from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.conf import settings

# User = get_user_model()

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login1(request):
    
    data=JSONParser().parse(request)
    username = data["username"]
    password = data["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.timezone import now
from rest_framework import generics, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .serializers import SnippetSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# @api_view(['POST'])
@csrf_exempt
def user_1(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt

def reset(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        if data["p1"]==data["p2"]:
            h=User.objects.filter(email=data["email"]).values("id")
            # f=User.objects.all()
            # if f:
            #     for i in f:
            #         if i.email==data["email"]:
            #             i.password=data["password"]
            #             i.save()
            #             return True
            #     else:
            #         return False
            # return "sdfdsf"
            if h:
                for i in h:
                    
                    User.objects.filter(id=i["id"]).update(password=data["p1"])
                    # User.save()
                    return JsonResponse({"passwordChanged":True}, status=200)
            else:
                return JsonResponse({"as":False}, status=400)

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
"""
this Api for aws sorage
"""
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TokenCreateView(utils.ActionViewMixin, generics.GenericAPIView):
#     """
#     Use this endpoint to obtain user authentication token.
#     """

#     serializer_class = settings.SERIALIZERS.token_create
#     permission_classes = settings.PERMISSIONS.token_create

#     def _action(self, serializer):
#         token = utils.login_user(self.request, serializer.user)
#         token_serializer_class = settings.SERIALIZERS.token
#         return Response(
#             data=token_serializer_class(token).data, status=status.HTTP_200_OK
#         )

# from djoser.views import views
class TokenDestroyView(views.APIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """

    # permission_classes = settings.PERMISSIONS.token_destroy

    def post(self, request):
        utils.logout_user(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


    # def permission_denied(self, request, message=None):
    #     if (
    #         settings.HIDE_USERS
    #         and request.user.is_authenticated
    #         and self.action in ["update", "partial_update", "list", "retrieve"]
    #     ):
    #         raise False
    #     super().permission_denied(request, message=message)

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = super().get_queryset()
    #     if settings.HIDE_USERS and self.action == "list" and not user.is_staff:
    #         queryset = queryset.filter(pk=user.pk)
    #     return queryset

    
    

#     @action(["post"], detail=False)
#     def activation(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.user
#         user.is_active = True
#         user.save()

#         signals.user_activated.send(
#             sender=self.__class__, user=user, request=self.request
#         )

#         if settings.SEND_CONFIRMATION_EMAIL:
#             context = {"user": user}
#             to = [get_user_email(user)]
#             settings.EMAIL.confirmation(self.request, context).send(to)

#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(["post"], detail=False)
#     def resend_activation(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.get_user(is_active=False)

#         if not settings.SEND_ACTIVATION_EMAIL or not user:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         context = {"user": user}
#         to = [get_user_email(user)]
#         settings.EMAIL.activation(self.request, context).send(to)

#         return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def set_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.request.user.set_password(serializer.data["new_password"])
        self.request.user.save()

        if settings.LOGOUT_ON_PASSWORD_CHANGE:
            utils.logout_user(self.request)

        if settings.PASSWORD_CHANGED_EMAIL_CONFIRMATION:
            context = {"user": self.request.user}
            to = [get_user_email(self.request.user)]
            settings.EMAIL.password_changed_confirmation(self.request, context).send(to)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user()

        if user:
            context = {"user": user}
            to = [get_user_email(user)]
            settings.EMAIL.password_reset(self.request, context).send(to)

        return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(["post"], detail=False)
#     def reset_password_confirm(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.user.set_password(serializer.data["new_password"])
#         if hasattr(serializer.user, "last_login"):
#             serializer.user.last_login = now()
#         serializer.user.save()

#         if settings.PASSWORD_CHANGED_EMAIL_CONFIRMATION:
#             context = {"user": serializer.user}
#             to = [get_user_email(serializer.user)]
#             settings.EMAIL.password_changed_confirmation(self.request, context).send(to)
#         return Response(status=status.HTTP_204_NO_CONTENT)

   