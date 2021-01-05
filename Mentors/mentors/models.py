from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Mentor(models.Model):
    crew_choices = (
        ('Solo', 'Solo'),
        ('Small', 'Small'),
        ('Large', 'Large'),
    )

    camera_choices = (
        ('Canon', 'Canon'),
        ('Nikon', 'Nikon'),
        ('Sony', 'Sony'),
        ('Red', 'Red'),
        ('Fuji', 'Fuji'),
        ('Panasonic', 'Panasonic'),
        ('Other', 'Other'),
    )

    category_choices = (
        ('Physics', 'Physics'),
        ('Web Development', 'Web Development'),
        ('Android Development', 'Android Development'),
        ('Chemistry', 'Chemistry'),
        ('Maths', 'Maths'),
        ('Commerce', 'Commerce'),
        ('Banking', 'Banking'),
        ('Software Development', 'Software Development'),
        ('CA/CS Exams', 'CA/CS Exams'),
        ('Arts', 'Arts'),
        ('Sciene', 'Sciene'),
        ('General Science', 'General Science'),
        ('Other', 'Other'),
    )

    first_name = models.CharField(max_length=260)
    last_name = models.CharField(max_length=260)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="media/mentors/%Y/%m")
    video_url = models.CharField(max_length=260)
    description = RichTextField()
    city = models.CharField(max_length=260)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=260)
    camera_type = models.CharField(choices=camera_choices, max_length=260)
    category = models.CharField(choices=category_choices, max_length=260)
    subs_count = models.CharField(max_length=260)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name
