from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfoModel(models.Model):
    #adds more fields to the default User class we imported
    user=models.OneToOneField(User)

    #additional classes

    portfolio_site= models.URLField(blank=True)#(blank=True) means that user doesnt need to fill this out

    profile_pic= models.ImageField(upload_to='profile_pics', blank=True)#upload_to='profile_pics' this needs to be a directory in the media directory

    def __str__(self):
        return self.user.username
