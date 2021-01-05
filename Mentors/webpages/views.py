from django.shortcuts import render
from .models import Slider, Team
from mentors.models import Mentor

# Create your views here.


def home_view(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_mentors = Mentor.objects.order_by(
        '-created_date').filter(is_featured=True)
    all_mentors = Mentor.objects.order_by('-created_date').all()

    context_data = {
        'sliders': sliders,
        'teams': teams,
        'featured_mentors': featured_mentors,
        'all_mentors': all_mentors,
    }

    return render(request, 'webpages/home.html', context_data)


def about_view(request):
    teams = Team.objects.all()
    context_data = {
        'teams': teams,
    }

    return render(request, 'webpages/about.html', context_data)


def services_view(request):
    return render(request, 'webpages/services.html', {})


def contact_view(request):
    return render(request, 'webpages/contact.html', {})
