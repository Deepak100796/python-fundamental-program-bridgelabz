from django.contrib import admin

# Register your models here.
# from socialAuth.models import SocialLogin
from . models import SocialLogin
admin.site.register(SocialLogin)