from django.contrib.auth.hashers import make_password
from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import UniqueConstraint


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=12, unique=True, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # (auth.E003) 'User.email' must be unique because it is named as the 'USERNAME_FIELD'.
    # Очевидно, можно указать email как уникальное поле
    # email = models.EmailField(unique=True)
    # или прописать SILENCED_SYSTEM_CHECKS = ['auth.E003', 'auth.W004'] в settings
    # или добавить constraints = [UniqueConstraint(fields=['username'], name='username_email')] в Meta
    # как сделал сейчас

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        constraints = [UniqueConstraint(fields=['email'], name='username_email')]
