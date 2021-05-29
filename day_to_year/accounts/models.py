from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length = 100)
    location = models.CharField(max_length = 200)
    phone_num = models.CharField(max_length=50)
    profile_img = models.ImageField(blank=True, null=True, upload_to ="accounts/")

