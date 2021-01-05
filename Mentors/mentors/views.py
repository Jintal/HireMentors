from django.shortcuts import render, get_object_or_404
from .models import Mentor

# Create your views here.


def mentors_view(request):
    mentors = Mentor.objects.order_by('-created_date').all()
    distinct_cities = Mentor.objects.values_list(
        'city', flat='True').distinct()
    distinct_cameras = Mentor.objects.values_list(
        'camera_type', flat='True').distinct()
    distinct_categories = Mentor.objects.values_list(
        'category', flat='True').distinct()

    context_data = {
        'mentors': mentors,
        'distinct_cities': distinct_cities,
        'distinct_cameras': distinct_cameras,
        'distinct_categories': distinct_categories,
    }
    return render(request, 'mentors/mentors.html', context_data)


def mentors_detail_view(request, id):
    mentor = get_object_or_404(Mentor, pk=id)
    context_data = {
        'mentor': mentor,
    }
    return render(request, 'mentors/mentors_detail.html', context_data)


def search_view(request):

    mentors = Mentor.objects.order_by('-created_date').all()
    distinct_cities = Mentor.objects.values_list(
        'city', flat='True').distinct()
    distinct_cameras = Mentor.objects.values_list(
        'camera_type', flat='True').distinct()
    distinct_categories = Mentor.objects.values_list(
        'category', flat='True').distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            mentors = mentors.filter(description__icontains=keyword)

    if 'searched_city' in request.GET:
        searched_city = request.GET['searched_city']
        if searched_city:
            mentors = mentors.filter(city__iexact=searched_city)

    if 'searched_camera_type' in request.GET:
        searched_camera_type = request.GET['searched_camera_type']
        if searched_camera_type:
            mentors = mentors.filter(
                camera_type__iexact=searched_camera_type)

    if 'searched_category' in request.GET:
        searched_category = request.GET['searched_category']
        if searched_category:
            mentors = mentors.filter(
                category__iexact=searched_category)

    context_data = {
        'mentors': mentors,
        'distinct_cities': distinct_cities,
        'distinct_cameras': distinct_cameras,
        'distinct_categories': distinct_categories,
    }
    return render(request, "mentors/mentors_search.html", context_data)
