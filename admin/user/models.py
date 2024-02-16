#from django.db import models
#from django.contrib.auth.models import AbstractUser
# Create your models here.

#class CustomUser(AbstractUser):

#	name = models.CharField(max_length=20, default='UserName')

#	email = models.EmailField(max_length=254, unique=True)

#	username = None

#	USERNAME_FIELD = 'email'

#	REQUIRED_FIELDS = ['email']

#	usr_phone = models.CharField(max_length=20)

#	usr_gender = models.CharField(max_length=10)

#	profile_pic = models.FileField(upload_to='profile/', default='profile/team.jpg')

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = None  # Remove the default username field

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    usr_phone = models.CharField(max_length=20)
    usr_gender = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='profile/', default='profile/team.jpg')  # Use ImageField instead of FileField for images

    objects = CustomUserManager()
