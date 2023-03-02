from django.urls import path
from Accounts import views

urlpatterns = [
    path('', views.LoginView ,name="Login"),
]