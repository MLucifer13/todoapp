from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model inheriting from AbstractUser. 
    This allows us to add additional fields to the user model.
    """
    bio = models.TextField(blank=True, null=True)  # Optional bio field for users

    def __str__(self):
        return self.username
