from django.db import models


class SocialLogin(models.Model):
    unique_id = models.CharField("Unique Id", max_length=500)
    provider = models.CharField("Service Provider", max_length=500)
    username = models.CharField("Username", max_length=500)
    full_name = models.CharField("Full name ", max_length=500)
    EXTRA_PARAMS = models.TextField("Extra Params", max_length=1000)

    def __str__(self):
        return self.provider + " " + self.username

    def __eq__(self, other):
        if isinstance(other, SocialLogin):
            return self.username == other.username
        return "cannot equalize different classes"

    def __repr__(self):
        return "SocialLogin({!r},{!r},{!r})".format(self.provider, self.username, self.unique_id)

    class Meta:
        verbose_name = "social login user"
        verbose_name_plural = "social login users"