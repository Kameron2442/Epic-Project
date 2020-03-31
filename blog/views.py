from django.shortcuts import render

posts = [
    {
        'l-id': '159',
        'u-id': '158',
        'date_cleaned': 'August 27, 2018',
        'description': 'Hello'
    },
    {
        'l-id': '159',
        'u-id': '158',
        'date_cleaned': 'August 27, 2018',
        'description': 'Hell'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
