from rest_framework.views import APIView
from .models import OTPModel
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from _applibs.utils import otp_generator
from datetime import datetime, timedelta
from .serializers import VerifyOtpSerializer

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

# {
#     "is_valid": True,
#     "msg": "Otp verify success",
#     "status_code": "OIV200"
# }

class VerifyOtpView(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        is_serializer_valid = serializer.is_valid()
        if is_serializer_valid is True:
            valid_data = serializer.validated_data
            phone_number = valid_data.get("phone_number")
            user_otp_number = valid_data.get("otp")

            otp_obj = OTPModel.objects.filter(
                otp_for="phone",
                identifier=phone_number,
            ).last()

            otp_code = otp_obj.otp_code

            if user_otp_number == otp_code:
                data = {
                    "is_valid": True,
                    "msg": "Otp verify success",
                    "status_code": "OIV200"
                }
            # else:
            #     data = {
            #         "is_valid": False,
            #         "msg": "Otp verify failed",
            #         "status_code": "OIV400"
            #     }
            
                return Response(data)
        
        data = {
            "is_valid": False,
            "msg": "Otp verify failed",
            "status_code": "OIV400"
        }
        return Response(data)

        # phone_number = request.data.get("phone_number")
        # otp_number = request.data.get("otp_number")


    



# expires_at = datetime.now() + timedelta(minutes=2)
# print(expires_at)
