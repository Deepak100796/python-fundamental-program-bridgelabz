from django.urls import path
# from .views import (SocialLoginView)
from . import views
urlpatterns = [
    # path("auth/", views.Oauth.as_view(), name="oauth"),
    # path("github/", views.Github.as_view(), name="github"),
    path('oauth/login/', views.SocialLoginView.as_view())
    ]