from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    birthdate=models.DateField(auto_now=False, auto_now_add=False)
    phonenumber=models.CharField(max_length=255)
    height=models.CharField(max_length=255)
    weight=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    