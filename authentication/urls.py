from django.urls import path, re_path
from . import views

# app_name = "authentication"
# username = "@" + str(username)

urlpatterns = [
    path("signin/", views.login, name="login"),
    path("onboarding/", views.onboarding, name="onboarding"),
    path("logout/", views.logout, name="logout"),
    path("profile/@<str:username>", views.profile, name="profile"),
]