from django.db import models


# Create your models here.
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from colorful.fields import RGBColorField

#
# from fundoo.settings import AUTH_USER_MODEL


# class UpdatedUser(AbstractUser):
#     image = models.ImageField(upload_to='image', default=None)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", default='admin')


class Label(models.Model):
    name = models.CharField("name of label", max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='label_user', default="admin")

    def __str__(self):
        return self.name
    #
    # def __eq__(self, other):
    #     if isinstance(other, Label):
    #         return self.name == other.name
    #     return "cannot equalize different classes"

    def __repr__(self):
        return "Label({!r},{!r})".format(self.user, self.name)

    class Meta:
        """
        name is given which will be displayed in admin page
        """
        verbose_name = 'label'
        verbose_name_plural = 'labels'


# Create your models here.
class Notes(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True, )
    note = models.CharField(max_length=500,blank=True)
    image = models.ImageField(max_length=500, blank=True, null=True, upload_to="media")
    is_archive = models.BooleanField("is_archived", default=False)
    is_trashed = models.BooleanField("delete_note", default=False)
    label = models.ManyToManyField(Label, related_name="label", blank=True)
    collaborators = models.ManyToManyField(User, related_name='collaborators', blank=True)
    is_copied = models.BooleanField("make a copy", default=False)
    checkbox = models.BooleanField("check box", default=False)
    is_pined = models.BooleanField("is pinned", default=False)
    url = models.URLField("url", blank=True)
    reminder = models.DateTimeField(blank=True, null=True)
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'], blank=True, null=True)

    def __str__(self):
        return self.note

    # def __eq__(self, other):
    #     if isinstance(other, Notes):
    #         return self.note == other.note
    #     return "cannot equalize different classes"

    def __repr__(self):
        return "Note({!r},{!r},{!r})".format(self.user, self.title, self.note)

    class Meta:
        """
        name is given which will be displayed in admin page
        """
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
