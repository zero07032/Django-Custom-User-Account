from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomeUserManager


ACCOUNT_TYPE_CHOICES = [
    ("ADMIN", "Admin"),
    ("TEACHER", "Teacher"),
    ("STUDENT", "Student"),
]


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        error_messages={"unique": "the email must be unique"},
    )
    post_ofice = models.CharField(max_length=250, null=True, blank=True)
    user_type = models.CharField(
        max_length=50, choices=ACCOUNT_TYPE_CHOICES, default="STUDENT"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.pk}.{self.email}"
