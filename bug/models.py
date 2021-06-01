from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



# Create your models here.
class BugUser(AbstractUser):
    is_developer       = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=True)