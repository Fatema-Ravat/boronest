from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE ,related_name='userprofile')
    image = models.ImageField(upload_to='users',blank=True,default='users/images/icon.png')
    apartment_name = models.CharField(max_length=500, default='MyApartment')
    apartment_number = models.CharField(max_length=100)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return self.user.username