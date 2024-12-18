from django.utils.timezone import now, timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("Users must have a phone number")
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    phone = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OTP(models.Model):
    phone = models.CharField(max_length=15, unique=False)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        return not self.is_used and self.created_at >= now() - timedelta(minutes=2)

    def __str__(self):
        return f"OTP for {self.phone}: {self.code}"


