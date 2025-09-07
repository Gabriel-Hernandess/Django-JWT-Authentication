from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    about = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    joined_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username