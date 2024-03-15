from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class IHaveUser(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.RESTRICT,
    )

    class Meta:
        abstract = True