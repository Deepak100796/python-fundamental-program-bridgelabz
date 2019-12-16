# from django.conf import settings

# from rest_framework import serializers
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response

# from requests.exceptions import HTTPError

# from social_django.utils import psa


# class SocialSerializer(serializers.Serializer):
#     """
#     Serializer which accepts an OAuth2 access token.
#     """
#     access_token = serializers.CharField(
#         allow_blank=False,
#         trim_whitespace=True,
#     )


# @api_view(http_method_names=['POST'])
# @permission_classes([AllowAny])
# @psa()
# def exchange_token(request, backend):
#     """
#     Exchange an OAuth2 access token for one for this site.
#     This simply defers the entire OAuth2 process to the front end.
#     The front end becomes responsible for handling the entirety of the
#     OAuth2 process; we just step in at the end and use the access token
#     to populate some user identity.
#     The URL at which this view lives must include a backend field, like:
#         url(API_ROOT + r'social/(?P<backend>[^/]+)/$', exchange_token),
#     Using that example, you could call this endpoint using i.e.
#         POST API_ROOT + 'social/facebook/'
#         POST API_ROOT + 'social/google-oauth2/'
#     Note that those endpoint examples are verbatim according to the
#     PSA backends which we configured in settings.py. If you wish to enable
#     other social authentication backends, they'll get their own endpoints
#     automatically according to PSA.
#     ## Request format
#     Requests must include the following field
#     - `access_token`: The OAuth2 access token provided by the provider
#     """
#     serializer = SocialSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         # set up non-field errors key
#         # http://www.django-rest-framework.org/api-guide/exceptions/#exception-handling-in-rest-framework-views
#         try:
#             nfe = settings.NON_FIELD_ERRORS_KEY
#         except AttributeError:
#             nfe = 'non_field_errors'

#         try:
#             # this line, plus the psa decorator above, are all that's necessary to
#             # get and populate a user object for any properly enabled/configured backend
#             # which python-social-auth can handle.
#             user = request.backend.do_auth(serializer.validated_data['access_token'])
#         except HTTPError as e:
#             # An HTTPError bubbled up from the request to the social auth provider.
#             # This happens, at least in Google's case, every time you send a malformed
#             # or incorrect access key.
#             return Response(
#                 {'errors': {
#                     'token': 'Invalid token',
#                     'detail': str(e),
#                 }},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         if user:
#             if user.is_active:
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             else:
#                 # user is not active; at some point they deleted their account,
#                 # or were banned by a superuser. They can't just log in with their
#                 # normal credentials anymore, so they can't log in with social
#                 # credentials either.
#                 return Response(
#                     {'errors': {nfe: 'This user account is inactive'}},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#         else:
#             # Unfortunately, PSA swallows any information the backend provider
#             # generated as to why specifically the authentication failed;
#             # this makes it tough to debug except by examining the server logs.
#             return Response(
#                 {'errors': {nfe: "Authentication Failed"}},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

from django.http import JsonResponse
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from requests.exceptions import HTTPError

from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from . import serializers
from django.contrib.auth import login
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
class SocialLoginView(generics.GenericAPIView):
    """Log in using facebook"""
    serializer_class = serializers.SocialSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Authenticate user through the provider and access_token"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.data.get('provider', None)
        strategy = load_strategy(request)

        try:
            backend = load_backend(strategy=strategy, name=provider,
            redirect_uri=None)

        except MissingBackend:
            return Response({'error': 'Please provide a valid provider'},
            status=status.HTTP_400_BAD_REQUEST)
        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get('access_token')
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response({
                "error": {
                    "access_token": "Invalid token",
                    "details": str(error)
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except AuthTokenError as error:
            return Response({
                "error": "Invalid credentials",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            authenticated_user = backend.do_auth(access_token, user=user)
        
        except HTTPError as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except AuthForbidden as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        if authenticated_user and authenticated_user.is_active:
			#generate JWT token
            login(request, authenticated_user)
            data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )}
			#customize the response to your needs
            response = {
                "email": authenticated_user.email,
                "username": authenticated_user.username,
                "token": data.get('token')
            }
            return Response(status=status.HTTP_200_OK, data=response)

# import pdb

# from django.contrib import auth
# from django.contrib.auth import login
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render, redirect

# # Create your views here.
# from authlib.integrations.requests_client import OAuth2Session
# from rest_framework.generics import GenericAPIView

# from fundoo.settings import SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET, AUTH_GITHUB_URL, AUTH_GITHUB_TOKEN_URL, \
#     BASE_URL, AUTH_GITHUB_USER_EMAIL_URL, AUTH_GITHUB_USER_URL, file_handler,logging
# from lib.redis import red
# from lib.token import token_validation
# from .models import SocialLogin

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)


# class Github(GenericAPIView):
#     """
#         Summary:
#         --------
#             Github class is a logic written where redirected url is github login page containing state and scope in header.
#         Methods:
#         --------
#             get: User will get a github login url page where he will enter git hub credentials
#     """

#     def get(self, request):
#         # pdb.set_trace()
#         resp = {'success': False, 'message': "something went wrong", 'data': []}
#         try:
#             auth_url = AUTH_GITHUB_URL
#             scope = 'user:email'
#             client = OAuth2Session(SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET, scope=scope)
#             url, state = client.create_authorization_url(auth_url)
#             logger.info("redirected user to github login page",)
#             return redirect(url)
#         except Exception as e:
#             logger.error("got %s error while redirecting the user to github login page ", str(e))
#             return HttpResponse(resp,status=404)


# class Oauth(GenericAPIView):
#     """
#       Summary:
#       --------
#           After user getting redirected to this class we will able to fetch token which will be created once we
#           provide client-key and client-secret. Once we fetch the token then we have to hit github user page and then
#           we will able to fetch user details excluding password
#       Methods:
#       --------
#           get: User details will be fetched after checking the access token
#     """
#     def get(self, request):

#         resp = {'success': False, 'message': "something went wrong", 'data': []}
#         try:
#             # pdb.set_trace()
#             token_url = AUTH_GITHUB_TOKEN_URL    # github token url.
#             scope = 'user:email'
#             client = OAuth2Session(SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET, scope=scope)

#             # here token is fetched after passing below params.
#             token = client.fetch_token(token_url, client_id=SOCIAL_AUTH_GITHUB_KEY, client_secret=SOCIAL_AUTH_GITHUB_SECRET
#                                        ,authorization_response=BASE_URL+request.get_full_path())
#             client = OAuth2Session(SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET, token=token,scope=scope)
#             account_url_email = AUTH_GITHUB_USER_EMAIL_URL
#             account_url= AUTH_GITHUB_USER_URL

#             # we will get response after hiting github url with proper access_token,code and state.
#             response = client.get(account_url)
#             response_email = client.get(account_url_email)

#             # response will contain all the details of the user which he authorised.
#             user_details=response.json()
#             email_id=response_email.json()[0]["email"]
#             username= response.json()["login"]
#             first_name = user_details["name"].split(" ")[0]
#             last_name = user_details["name"].split(" ")[1]

#             # first we will check if we have registered this user if yes then we will generate JWT token and redirect.
#             if SocialLogin.objects.filter(unique_id=response.json()["id"]).exists():
#                 user = auth.authenticate(username=username, password=response.json()["id"])
#                 token = token_validation(user.username, response.json()["id"])
#                 auth.login(request, user)
#                 red.set(user.username, token)
#                 logger.info("%s logged in using social auth ",user.username)
#                 # return redirect("/api/notes/")
#             else:

#                 # if we have not registered this user then we save user details in SocialLogin page.
#                 SocialLogin.objects.create(unique_id=response.json()["id"], provider="github", full_name=user_details["name"],
#                                            username=username, EXTRA_PARAMS=response.json())

#                 # if registered user has same user name matching in db then we will use his unique_id as username and
#                 # save the user.
#                 if User.objects.filter(username=username).exists():

#                     user = User.objects.create_user(username=response.json()["id"], first_name=first_name, last_name=last_name,
#                                                     email=email_id, password=response.json()["id"])
#                     user.save()
#                     token = token_validation(username, response.json()["id"])
#                     red.set(user.username, token)
#                     logger.info("%s logged in as well as user got registered but username already exixt so his id "
#                                 "is as his username ", user.username)
#                 else:

#                     # here we will save the user details and generate jwt token and then redirect to dashboard.
#                     user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
#                                                     email=email_id,password=response.json()["id"])
#                     user.save()
#                     token = token_validation(username, response.json()["id"])
#                     red.set(user.username, token)
#                     logger.info("%s logged in as well as user got registered ", user.username)

#             # once user is registered or logged in user is redirected to dashboard
#             return redirect("/api/notes/")
#         except Exception as e:
#             logger.error("error: %s while registering user or while logging in ",str(e))
#             return HttpResponse(resp ,status=404)