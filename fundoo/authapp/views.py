from django.shortcuts import render

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
from . models import User
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


from .serializers import SnippetSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# @api_view(['POST'])
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
#     data=request.DATA
#     print(data)
#     return JsonResponse({"da:":"True"})
#     VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
#     DEFAULTS = {
#         # you can define any defaults that you would like for the user, here
#     }
#     serialized = UserSerializer(data=request.DATA)
#     if serialized.is_valid():
#         user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
#         user_data.update(DEFAULTS)
#         user = get_user_model().objects.create_user(
#             **user_data
#         )
#         return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


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



