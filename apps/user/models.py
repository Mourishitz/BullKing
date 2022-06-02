from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import DIET_CHOICES, GENDER_CHOICES


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    birthday = models.DateField(blank=True, null=True, auto_now_add=False)
    username = models.CharField(max_length=150, blank=True, null=True, editable=False, unique=True)
    diet = models.CharField(max_length=3, choices=DIET_CHOICES, default='1')
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default='3')
