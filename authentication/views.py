from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.models.user import user
from django.contrib import auth
# from django.contrib import logout
from django.contrib import messages

# Create your views here.

# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )



@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponse(f"Hello {user}")


def onboarding(request):
    return render(request, "authentication/get-started.html")

def login(request):

    if request.method == "GET":
        request.session["login_from"] = request.META.get('HTTP_REFERER', '/')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user:
            # User is authenticated
            auth.login(request, user)
            # return render(request, "index.html")
            return HttpResponseRedirect(request.session['login_from'])
            
        else:
            messages.error(request, "Incorrect Password/Username. Please check your credentials and try again!")
            return render(request, 'authentication/login.html')
    else:
        if request.user.is_authenticated == True:
            return redirect("home")

    return render (request, "authentication/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
