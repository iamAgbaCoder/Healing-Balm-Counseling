from django.shortcuts import render, redirect
from django.contrib import messages 

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import activate

import requests
# fetch db tables from database  
from .models import *

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from smtplib import SMTPException
import smtplib

import socket 

from django.contrib.sites.shortcuts import get_current_site

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )

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

    context = {"testimonies": testimony, "counsellors": counsellor} # pass data from database to frontend 
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

        subject=f"[APPOINTMENT REQUEST ALERT] Counselling Appointment Booking from {name}"
        message=f"Name: {name}\nEmail: {email}\nGender: {gender}\nPhone: {phone}\nAge Range: {age_range}\nChallenge Facing: {challenge}\nDesired Date of Appointment: {date_of_appointment}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email, from_email]

        try:
            send_mail( subject, message, from_email, recipient_list, fail_silently=False)
            appointment.save();
        except BadHeaderError as e:
            messages.error(request, "Oops! An Error Occurred {e}. Please Try Again")


        print(recipient_list)
        print("sent")
        
        # show_toast = "Your request has been received and processed successfully. Please check your mail for further instructions. Thank you✅"
        messages.success(request, "Your request has been received and processed successfully. Please check your mail for further instructions. Thank you✅")
        # context = {"show_toast": show_toast}
        return render(request, "index.html",  context)
        
    return render(request, "index.html", context)

def about_us(request):
    context = {"picture_excerpts": picture_excerpts}
    return render(request, "about.html", context)

def contact_us(request):
    
    site = get_current_site(request)
    print(site)

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact_subject = request.POST["subject"]
        contact_message = request.POST["message"]

        if contact_subject == "":
            subject = f"[MESSAGE ALERT FROM YOUR WEBSITE - {site}]"
        else:
            subject = f"[MESSAGE ALERT FROM YOUR WEBSITE - {site}] {contact_subject}"
        
        message = f"Name: {name}\n\nMessage: {contact_message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email, from_email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, "Your request has been received and processed successfully. Please check your mail for further instructions. Thank you✅")
        except (BadHeaderError, SMTPException) as e:
            if isinstance(e.args[0], socket.gaierror):
                messages.error(request, "Oops! Hostname cannot be resolved. Please Try Again Later")
            messages.error(request, "Oops! An error occured {e}. Please Try Again")
            return redirect("contact")

    return render(request, "contact.html")


def services(request):
    context = {"testimonies": testimony}
    return render(request, "services.html", context)