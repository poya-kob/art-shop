from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from django.http.response import HttpResponseRedirect

from .models import User

from utils.validators import otp_validator

UserModel: User = get_user_model()


class LoginUser(APIView):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.request.DATA.get('next', '/'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        phone_number = self.request.data['phone_number']
        next_url = self.request.POST.get('next', '/')
        otp = self.request.data['otp']
        if otp_validator(otp, phone_number):
            user = UserModel.objects.get(mobile_number__exact=phone_number)
            login(request, user)
            return HttpResponseRedirect(redirect_to=next_url)
        return Response(_('phone or otp is not correct'), status=status.HTTP_400_BAD_REQUEST)


@login_required()
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
