from django.contrib import admin
from .models import OTPModel


@admin.register(OTPModel)
class OtpAdmin(admin.ModelAdmin):
    list_display = (
        "otp_for",
        "identifier",
        "reason",
        "status",
        "expires_at",
    )
