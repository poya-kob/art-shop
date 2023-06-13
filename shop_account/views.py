from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, login, logout
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from django.http.response import HttpResponseRedirect

from .models import User
from utils.validators import otp_validator
from utils.mixins import UserNotLoggedInMixin
from .serializers import RegisterUserSerializer

UserModel: User = get_user_model()


class LoginUser(UserNotLoggedInMixin, APIView):
    def get(self, request):
        if mobile_number := self.request.data.get('mobile_number', False):
            user = UserModel.objects.filter(mobile_number=mobile_number)
            if user.exists():
                otp = user.first().set_otp()
                return Response({'message': _('otp have been send successfully!!'),
                                 'otp': otp})

    def post(self, request):
        mobile_number = self.request.data['mobile_number']
        next_url = self.request.POST.get('next', '/')
        otp = self.request.data['otp']
        if otp_validator(otp, mobile_number):
            return self._active_user(mobile_number, next_url)
        return Response(_('phone or otp is not correct'), status=status.HTTP_400_BAD_REQUEST)

    def _active_user(self, mobile_number, next_url):
        user = UserModel.objects.get(mobile_number__exact=mobile_number)
        if not user.is_active:
            user.is_active = True
        user.otp_last_login = datetime.now()
        user.save()
        login(self.request, user)
        return HttpResponseRedirect(redirect_to=next_url)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response(_('User Logged out successfully'))


class RegisterUser(UserNotLoggedInMixin, APIView):

    def post(self, request):
        serializer = RegisterUserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            if not serializer.errors:
                return Response({'message': _('user created successfully login to active user'),
                                 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({'error': _('not valid data or mobile number registered before!')},
                        status=status.HTTP_400_BAD_REQUEST)
