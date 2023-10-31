from django.contrib import admin
from .models import Testimony, Appointment, Counsellor, PictureExcerpt

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Counsellor)
admin.site.register(Testimony)
admin.site.register(PictureExcerpt)