from django.urls import path, re_path
from . import views

# app_name = "authentication"

urlpatterns = [
    path("signin/", views.login, name="login"),
]