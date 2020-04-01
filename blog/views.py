from django.shortcuts import render
from .models import Location
from .models import Cleaned

#<if L_id == loc.id{}>

def home(request):
    context = {
        'locations': Location.objects.all(),
        'cleaned': Cleaned.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
