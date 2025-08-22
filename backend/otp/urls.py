from django.urls import path
from .views import OtpSendView

urlpatterns = [
    # http://127.0.0.1:8001/otp/send/
    path(
        route="send/",
        view=OtpSendView.as_view(),
        name="otp_send"
    ),
]