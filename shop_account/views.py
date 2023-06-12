import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from django.http.response import HttpResponseRedirect

from .models import User
from utils.validators import otp_validator
from utils.mixins import UserNotLoggedInMixin
from .serializers import RegisterUserSerializer

UserModel: User = get_user_model()


class LoginUser(APIView, UserNotLoggedInMixin):

    def post(self, request):
        mobile_number = self.request.data['mobile_number']
        next_url = self.request.POST.get('next', '/')
        otp = self.request.data['otp']
        if otp_validator(otp, mobile_number):
            user = UserModel.objects.get(mobile_number__exact=mobile_number)
            login(request, user)
            return HttpResponseRedirect(redirect_to=next_url)
        return Response(_('phone or otp is not correct'), status=status.HTTP_400_BAD_REQUEST)


@login_required()
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


class RegisterUser(APIView, UserNotLoggedInMixin):

    def post(self, request):
        serializer = RegisterUserSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            if not serializer.errors:
                return Response({'message': 'user created successfully',
                                 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({'error': _('not valid data or mobile number registered before!')},
                        status=status.HTTP_400_BAD_REQUEST)
