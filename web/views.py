from django.shortcuts import render, redirect
from django.contrib import messages 

# fetch db tables from database  
from .models import *

# Create your views here.

# fetchs all data in Database Models(DB Table)
testimony = Testimony.objects.all().order_by("date_created")
counsellor = Counsellor.objects.all()
picture_excerpts = PictureExcerpt.objects.all()

def homepage(request):
    
    context = {"testimonies": testimony, "counsellors": counsellor} # pass data from database to frontend 
    
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
                messages.error(request, f"Oops! An appointment already exist with this name and email address. Please try again with a different name or email.")
                return render(request, "index.html", context)
                
        appointment = Appointment.objects.create(name=name, email=email, gender=gender, phone=phone, challenge=challenge, age_range=age_range, date_of_appointment=date_of_appointment)   
        appointment.save();
        
        messages.success(request, "Your request has been received and processed successfully. Please check your mail for further instructions. Thank you✅")
        return render(request, "index.html", context)
        
        
    return render(request, "index.html", context)

def about_us(request):
    context = {"picture_excerpts": picture_excerpts}
    return render(request, "about.html", context)

def contact_us(request):
    return render(request, "contact.html")


def services(request):
    context = {"testimonies": testimony}
    return render(request, "services.html", context)