from django.shortcuts import render, redirect
from django.contrib import messages 

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import activate

import requests
# fetch db tables from database  
from .models import *

# Create your views here.

# fetchs all data in Database Models(DB Table)
testimony = Testimony.objects.all().order_by("date_created")
counsellor = Counsellor.objects.all()
picture_excerpts = PictureExcerpt.objects.all()


def switch_language(request, language_code):
    
    request.session['language_code'] = language_code
    request.session['modal_shown'] = True  # Store a flag indicating the modal has been shown
    
    activate(language_code)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))
    response.set_cookie('language_code', language_code, max_age=3600*24*30)  # Set the cookie to expire after 30 days
    return response




def homepage(request):    
    
    user_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0]
    print(user_language)
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        age_range = request.POST["age"]
        challenge = request.POST["challenge"]
        date_of_appointment = request.POST["date"]  
        
        if Appointment.objects.filter(name=name).exists():
            if Appointment.objects.filter(email=email).exists():
                show_toast = "Oops! An appointment already exist with this name and email address. Please try again with a different name or email."
                # context = {"show_toast": show_toast}
                messages.error(request, f"Oops! An appointment already exist with this name and email address. Please try again with a different name or email.")
                return render(request, "index.html", context)
                
        appointment = Appointment.objects.create(name=name, email=email, gender=gender, phone=phone, challenge=challenge, age_range=age_range, date_of_appointment=date_of_appointment)   
        appointment.save();
        
        # show_toast = "Your request has been received and processed successfully. Please check your mail for further instructions. Thank you✅"
        messages.success(request, "Your request has been received and processed successfully. Please check your mail for further instructions. Thank you✅")
        # context = {"show_toast": show_toast}
        return render(request, "index.html",  context)
        
    context = {"testimonies": testimony, "counsellors": counsellor} # pass data from database to frontend 
    return render(request, "index.html", context)

def about_us(request):
    context = {"picture_excerpts": picture_excerpts}
    return render(request, "about.html", context)

def contact_us(request):
    return render(request, "contact.html")


def services(request):
    context = {"testimonies": testimony}
    return render(request, "services.html", context)