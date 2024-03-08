from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.


class PetstagramUser(auth_models.AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        
    )
