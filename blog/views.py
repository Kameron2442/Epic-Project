from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Location
from .models import Cleaned
#from django.urls import reverse


def home(request):
    context = {
        'locations': Location.objects.all(),
        'cleaned': Cleaned.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostDetailView(DetailView):
    model = Location

class PostUpdateView(UpdateView):
    model = Location 
    fields = ['l_name', 'x_cord', 'y_cord', 'description', 'times_cleaned']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(CreateView):
    model = Location 
    #success_url = reverse('blog-home')
    #success_url = '../../'
    fields = ['l_name', 'x_cord', 'y_cord', 'description', 'times_cleaned']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    success_url = '/'
    model = Location

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
