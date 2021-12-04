from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,name, email,username, password=None):
        if not email:
            raise ValueError("User must have email!")

        email = self.normalize_email(email)
        user = self.model(name=name,email=email,username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,name, email,username, password):
        user = self.create_user(name, email,username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255,default="",null=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50,default="",null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","username"]
    
    
    def __str__(self):
        return self.email


class profileInfo(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    dateOfBirth = models.DateField()
    age = models.IntegerField()
    proffession = models.CharField(max_length=100,default="",null=False)
    sex = models.CharField(max_length=10,default="",null=False)
    height = models.CharField(max_length=20,default="",null=False)
    religion = models.CharField(max_length=50,default="",null = False)


    def __str__(self):
        return  f'{self.user.username} profile'