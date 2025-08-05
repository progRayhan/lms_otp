from django.db import models


class OtpStatus(models.TextChoices):
    INITIALIZE = "INITIALIZE"
    VERIFIED = "VERIFIED"
    EXPIRED = "EXPIRED"
    