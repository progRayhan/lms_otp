from rest_framework.views import APIView
from .models import OTPModel
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from _applibs.utils import otp_generator
from datetime import datetime, timedelta

class OtpSendView(APIView):
    def post(self, request):
        request_data = request.data

        otp = otp_generator()

        current_time = datetime.now()
        after_two_minuites = timedelta(minutes=2)

        OTPModel.objects.create(
            otp_for=request_data.get("otp_for"),
            identifier=request_data.get("identifier"),
            reason=request_data.get("reason"),
            otp_code=otp,
            message=f"Your OTP is {otp}",
            expires_at=current_time+after_two_minuites,
        )

        # send otp to the user

        return Response({
            "msg": "Success",
            "data": "Otp Successfully Send"
        })




# expires_at = datetime.now() + timedelta(minutes=2)
# print(expires_at)
