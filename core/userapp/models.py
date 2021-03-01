from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email,  username, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            ** extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, username, password,
                                **extra_fields)

    def create_superuser(self, email, username, password,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.BigIntegerField(verbose_name='Mobile or Email', unique=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.email} Profile'
