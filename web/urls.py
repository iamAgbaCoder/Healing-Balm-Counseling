from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about-us/", views.about_us, name="about"),
    path("contact-us/", views.contact_us, name="contact"),
    path("services/", views.services, name="services")
]