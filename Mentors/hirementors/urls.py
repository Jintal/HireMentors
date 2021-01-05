from django.urls import path
from . import views

urlpatterns = [
    path('hirementor', views.hirementor_view, name='hirementor'),

]
