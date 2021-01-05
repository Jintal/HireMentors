from django.shortcuts import render, redirect
from .models import Hirementor
from django.contrib import messages

# Create your views here.


def hirementor_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mentor_id = request.POST['tuber_id']
        mentor_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hirementor = Hirementor(first_name=first_name, last_name=last_name,
                                mentor_id=mentor_id, mentor_name=mentor_name, city=city, phone=phone, email=email, state=state, message=message, user_id=user_id)
        hirementor.save()
        messages.success(request, "Thanks for reaching out to us!!!")
        return redirect('home')
