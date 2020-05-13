from django.shortcuts import render

posts = [
    {
        'author': 'Kevin Powell',
        'title': 'The real G.O.A.T',
        'content': 'Muhammad Ali', 
        'date_posted': 'May 9th, 2020'
    },
    {
        'author': 'Lazy Couch',
        'title': 'The real G.O.A.T',
        'content': 'Michael Jordan', 
        'date_posted': 'May 11th, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')
