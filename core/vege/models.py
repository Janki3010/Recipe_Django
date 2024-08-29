from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=20)
    receipe_des = models.TextField()
    receipe_image = models.ImageField()
