from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Superheroes(models.Model):
    nick = models.CharField(max_length=50)
    real_name = models.CharField(max_length=100)
    power = models.IntegerField()
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nick

class AuthUser(AbstractUser):
   
    pass
