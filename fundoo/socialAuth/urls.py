from django.urls import path
from .views import (SocialLoginView)
urlpatterns = [
    path('', SocialLoginView.as_view())
    ]