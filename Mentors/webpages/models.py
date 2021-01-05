from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=260)
    last_name = models.CharField(max_length=260)
    role = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=260)
    linkedin_link = models.CharField(max_length=260)
    photo = models.ImageField(upload_to="media/team/%Y")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=260)
    subtitle = models.CharField(max_length=260)
    button_text = models.CharField(max_length=260)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    redirect_link = models.URLField(default="https://www.ubuntu.com")

    def __str__(self):
        return self.headline
