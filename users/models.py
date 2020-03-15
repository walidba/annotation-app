from django.db import models
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexe  = models.CharField(max_length=6,choices=[('male','Male'), ('f','Female')],default='female') 
    age = models.IntegerField()
    def __str__(self):
        return self.user.username
