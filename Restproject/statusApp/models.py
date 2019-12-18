from django.db import models

def upload_status_image(instance, filename):
    return "updates/{user}/{filename}".format(user= instance.user, filename=filename)

# Create your models here.
class Status(models.Model):
    user    = models.ForeignKey()
    content = models.TextField(null=True,blank=True)
    image   = models.ImageField(upload_to = upload_status_image, null=True, blank = True)
