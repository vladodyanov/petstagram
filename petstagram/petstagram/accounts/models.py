from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models
from petstagram.accounts.managers import PetstagramUserManager

from django.utils import timezone


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = PetstagramUserManager()


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    user = models.OneToOneField(
        PetstagramUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
