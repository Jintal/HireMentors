from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentors_view, name="mentors"),
    path('<int:id>', views.mentors_detail_view, name="mentors_detail"),
    path('search', views.search_view, name="search"),

]
