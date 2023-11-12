from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib import logout
from django.contrib import messages

# Create your views here.


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user:
            # User is authenticated
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Incorrect Password/Username. Please check your credentials and try again!")
            return render(request, 'authentication/login.html')

    return render (request, "authentication/login.html")


# def logout(request):
