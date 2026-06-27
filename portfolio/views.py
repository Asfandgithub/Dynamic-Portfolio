from django.shortcuts import render
from .models import *

def home(request):

    context = {
        'profile': Profile.objects.first(),
        'education': Education.objects.all(),
        'skills': Skill.objects.all(),
        'languages': Language.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }

    return render(request, 'index.html', context)

from .models import Skill

def home(request):
    skills = Skill.objects.all().order_by('category')

    context = {
        'skills': skills,
    }

    return render(request, 'home.html', context)