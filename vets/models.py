from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['email', 'first_name']
    USERNAME_FIELD = 'username'
    

    def __str__(self):
        return self.username
