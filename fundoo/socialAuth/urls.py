from django.urls import path
from .views import (SocialLoginView)
urlpatterns = [
    path('login/', SocialLoginView.as_view())
    ]