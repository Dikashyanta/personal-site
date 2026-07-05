from django.shortcuts import render
from .models import HeroSection, Interest, Memory

def about(request):
    hero = HeroSection.objects.first()
    interests = Interest.objects.select_related('category').all().order_by('category__name')
    memories = Memory.objects.all().order_by('-date')
    
    context = {
        'hero': hero,
        'interests': interests,
        'memories': memories,
    }
    return render(request, 'about/about.html', context)
