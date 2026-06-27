from django.shortcuts import render
from .models import *

def home(request):

    context = {
        'profile': Profile.objects.first(),
        'contact': Contact.objects.first(),
        'education': Education.objects.all(),
        'skills': Skill.objects.all(),
        'languages': Language.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }

    return render(request, 'index.html', context)