from django.conf import settings
from django.db import models

def upload_status_image(instance, filename):
    return "updates/{user}/{filename}".format(user= instance.user, filename=filename)
class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

# Create your models here.
class Status(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    content   = models.TextField(null=True,blank=True)
    image     = models.ImageField(upload_to = upload_status_image, null=True, blank = True)
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)[:50]
          