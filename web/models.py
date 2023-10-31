from django.db import models

# Image Processing and Manipulation
from PIL import Image

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    phone = models.CharField(max_length=14)
    age_range = models.CharField(max_length=12)
    challenge = models.CharField(max_length=15)
    date_of_appointment = models.DateField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # db_table = ''
        managed = True
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'    
        ordering = ("-date_created",)
        
    def __str__(self) -> str:
        return f"{self.name}'s Appointment"
    

class Counsellor(models.Model):
    name =  models.CharField(max_length=20)
    specialization = models.CharField(max_length=50)
    short_bio = models.CharField(max_length=100, help_text="Bio should be short, precise and detailed - Max 100 characters")
    image = models.ImageField(upload_to="counsellors/")
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # db_table = ''
        managed = True
        verbose_name = 'Counsellor'
        verbose_name_plural = 'Counsellors'
        ordering = ("-date_added", )
        
    def __str__(self) -> str:
        return f"{self.name}'s Profile"


class Testimony(models.Model):
    name = models.CharField(max_length=30, default="Anonymous")
    title = models.CharField(max_length=50, help_text="e.g Deliverance from depression. Short and precise.")
    testimony = models.TextField()
    location = models.CharField(max_length=20, default="Unknown", help_text="State, Country - e.g Lagos, Nigeria")
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="logo.png", upload_to="testimonials/")
    
    def __str__(self) -> str:
        return f"{self.name}'s Testimony"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image)
        
        if img.height > 100 or img.width > 100:
            size = (100, 100)
            img.thumbnail(size)
            img.save(self.image.path, quality=100)
            img.close()
            self.image.close()
    
    class Meta:
        verbose_name = "Testimony"
        verbose_name_plural = "Testimonies"
        ordering = ("-date_created",)
        

class PictureExcerpt(models.Model):
    image = models.ImageField(null=False, upload_to="images/")
    title = models.CharField(max_length=100, help_text="short informations about the image. NOTE: this field can be ignored", blank=True)
    
    def __str__(self) -> str:
        return self.image.name
    
    class Meta:
        # db_table = ''
        managed = True
        verbose_name = 'Picture Excerpt'
        verbose_name_plural = 'Picture Excerpts'
    