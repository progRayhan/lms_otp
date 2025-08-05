from django.db import models
from _applibs.model_choice_fields import OtpStatus


class OTPModel(models.Model):
    otp_for = models.CharField(max_length=50)
    identifier = models.CharField(max_length=100)
    reason = models.CharField(max_length=60)
    otp_code = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20, 
        choices=OtpStatus.choices, 
        default=OtpStatus.INITIALIZE
    )
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.otp_code
    
    class Meta:
        verbose_name = "Otp"
        verbose_name_plural = "Otps"
        db_table = "otp"
    