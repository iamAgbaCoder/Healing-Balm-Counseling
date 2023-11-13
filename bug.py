# settings.py
LOGIN_URL = '/auth/signin/'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/' 

# urls.py
urlpatterns = [
    path("signin/", views.login, name="login"),
    path("onboarding/", views.onboarding, name="onboarding"),
    path("logout/", views.logout, name="logout"),
    path("profile/@<str:username>", views.profile, name="profile"),
]


# views.py 
@login_required # User profile view
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return HttpResponse(f"Hello {user}")


def login(request): # login view

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

    return render (request, "authentication/login.html")

# these blocks of codes are created to redirect users to pages restricted
# to unauthenticated users. Users are first authenticated and 
# then directed to the page using this URL path below 
# http://127.0.0.1:8000/auth/signin/?next=/en/auth/profile/johndoe

# but it's not working, help! 😫😭
# Tech is HARD!! 😭😭😭