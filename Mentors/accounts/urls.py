from django.urls import path, include

from . import views

urlpatterns = [
    path('user_login', views.user_login_view, name="login"),
    path('user_register', views.user_register_view, name="register"),
    path('user_logout', views.user_logout_view, name="logout"),
    path('dashboard', views.dashboard_view, name="dashboard"),
]
