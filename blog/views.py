from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Location
from .models import Cleaned
#from django.urls import reverse
from django.db import connection


def home(request):
    context = {
        'locations': Location.objects.all(),
        'cleaned': Cleaned.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):

    allLoc = []
    for p in Location.objects.raw('SELECT * FROM blog_location'):
        allLoc.append(p)

    avgCleans = []
    for p in Cleaned.objects.raw('SELECT id, avg(total) as average from (SELECT id, l_id_id, COUNT(*) as total FROM blog_cleaned GROUP BY l_id_id)'):
        avgCleans.append(p)

    viewLoc = []
    myVar = ('2',)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM locandcleans WHERE times_cleaned > ?", myVar)
        row = cursor.fetchall()
        for i in row:
            print(i)
            viewLoc.append(i[0] + " was cleaned " + str(i[1]) + " times")


    context = {
        'title': 'About',
        'allLoc': allLoc,
        'avgCleans': avgCleans,
        'viewLoc': viewLoc
    }
    return render(request, 'blog/about.html', context)

class PostDetailView(DetailView):
    model = Location

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['cleans'] = Cleaned.objects.all()
        return context

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


class PostCreateClean(CreateView):
    model = Cleaned 
    fields = ['date_cleaned', 'description']
    #success_url = '../'
    def form_valid(self, form):
        form.instance.u_id = self.request.user
        form.instance.l_id = get_object_or_404(Location, l_id=self.kwargs['pk'])
        return super().form_valid(form)


def server_error(request):
    context = {}
    return render(request, 'blog/500.html', context, status=500)

#    l_id = models.ForeignKey(Location, on_delete = models.CASCADE)
#     u_id = models.ForeignKey(User, on_delete = models.CASCADE)
#     date_cleaned = models.DateTimeField(default = timezone.now)
#     description = models.TextField()
