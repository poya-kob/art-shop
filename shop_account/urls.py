from django.urls import path
import views

urlpatterns = [
    path('login-user/',views.LoginUser.as_view(),name='login-user' ),
    path('logout-user/',views.logout_user,name='logout-user' ),
]