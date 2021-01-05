from django.shortcuts import render, redirect
from .models import Contact_Tuber
from django.contrib import messages
# Create your views here.


def contact_tubers_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']

    contact_tuber = Contact_Tuber(full_name=full_name, phone=phone, email=email,
                                  company_name=company_name, subject=subject, message=message, user_id=user_id)
    contact_tuber.save()
    messages.success(request, "Thanks for reaching out to us!!!")
    return redirect('home')
