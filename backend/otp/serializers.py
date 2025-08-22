from rest_framework import serializers


class VerifyOtpSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        max_length=16,
        regex=r'^(?:\+8801|01)[3-9]\d{8}$',
        error_messages={
            'invalid': 'Enter a valid Bangladeshi phone number (e.g., +8801XXXXXXXXX or 01XXXXXXXXX).'
        }
    )
    otp = serializers.CharField(max_length=6)
    