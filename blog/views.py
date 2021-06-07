from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#post array of dictionary

posts = [
    {
        'authoe': 'dhruv singhal',
        'title': 'time management',
        'body': 'dm me for effective time management strategies',
        'date_published' : '2nd Jan, 2021'
    },
    {
        'author': 'aayush singhal',
        'title': 'JEE preparation',
        'body': 'dm me for effective time JEE strategies',
        'date_published' : '8th Jan, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
