from django.db import models

# Create your models here.

# full_name = request.POST['full_name']
# phone = request.POST['phone']
# email = request.POST['email']
# company_name = request.POST['company_name']
# subject = request.POST['subject']
# message = request.POST['message']
# user_id = request.POST['user_id']


class Contact_Tuber(models.Model):
    full_name = models.CharField(max_length=260)
    phone = models.IntegerField()
    email = models.EmailField()
    company_name = models.CharField(max_length=260)
    subject = models.CharField(max_length=260)
    message = models.TextField()
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.full_name
