from django.db import models

# Create your models here.
class User(models.Model):
    first_name       = models.CharField(max_length=50)
    last_name        = models.CharField(max_length=50)
    email            = models.CharField(max_length=100)
    password         = models.CharField(max_length=100)
    conferm_password = models.CharField(max_length=100)



# from django.db import models


# from django.db import models

# class Document(models.Model):
#     # uploaded_at = models.DateTimeField(auto_now_add=True)
#     uploadind= models.FileField()


# class MyFile(models.Model):
#     file = models.FileField(blank=False, null=False)
#     description = models.CharField(max_length=50)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)