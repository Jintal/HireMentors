from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in successfully!!!")
            return redirect("dashboard")
        else:
            messages.warning(request, "Invalid credentials!!!")
            return redirect("login")

    return render(request, 'accounts/user_login.html')


def user_register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(
                    request, "Username exists, please use another!!!")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(
                        request, "Email exists, please use another!!!")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    messages.success(
                        request, "Account Created Successfully!!!")
                    return redirect("login")
        else:
            messages.warning(request, "Passwords do not match!!!")
            return redirect("register")

    return render(request, 'accounts/user_register.html')


def user_logout_view(request):
    logout(request)
    messages.success(
        request, "Logged Out Successfully!!!")
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
