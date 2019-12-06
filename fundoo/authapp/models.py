from django.db import models

# Create your models here.
class User(models.Model):
    first_name       = models.CharField(max_length=50)
    last_name        = models.CharField(max_length=50)
    email            = models.CharField(max_length=100)
    password         = models.CharField(max_length=100)
    conferm_password = models.CharField(max_length=100)



from django.db import models


class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()