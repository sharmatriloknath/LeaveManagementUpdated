from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_ROLE = (
        ("employee", "Employee"),
        ("Manager", "Manager"),
        ("hr", "HR"),
    )
    username = None
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)
    role = models.CharField(max_length=10, choices=USER_ROLE, null=False, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        # return f"{self.email} - {self.first_name} {self.last_name}"
        pass


class Leaves(models.Model):
    LEAVE_TYPE = (("cl", "Casual Leaves"), ("el", "Earned Leaves"), ("sl", "Sick Leaves"), ("ml", "Maternity Leaves"))
    LEAVE_STATUS = [("draft", "Draft"), ("sent_for_approval", "Send For Approval"), ("approved", "Approved"), ("cancel", "Cancel")]
    name = models.CharField(max_length=50, blank=True, default='Users Leaves')
    leave_type = models.CharField(max_length=5, choices=LEAVE_TYPE)
    state = models.CharField(max_length=20, choices=LEAVE_STATUS)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    requested_days = models.FloatField()
    allocated_days = models.FloatField()
    remaining_leaves = models.FloatField()
    allocation_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''+str(self.name)


