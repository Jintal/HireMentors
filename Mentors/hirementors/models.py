from django.db import models
from datetime import datetime
# Create your models here.


class Hirementor(models.Model):
    first_name = models.CharField(max_length=260)
    last_name = models.CharField(max_length=260)
    mentor_id = models.IntegerField(blank=True)
    mentor_name = models.CharField(max_length=260)
    city = models.CharField(max_length=260)
    phone = models.CharField(max_length=260)
    email = models.EmailField()
    state = models.CharField(max_length=260)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
