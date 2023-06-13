from django.urls import path
from .views import LoginUser,RegisterUser,logout_user

urlpatterns = [
    path('login-user/', LoginUser.as_view(), name='login-user'),
    path('logout-user/', logout_user, name='logout-user'),
    path('register-user/', RegisterUser.as_view(), name='register-user'),
]