
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.registration,name="registration"),
    path('',views.base,name="home"),
    path('logout',views.user_logout,name="user_logout"),
]
