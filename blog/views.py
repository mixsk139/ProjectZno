from django.shortcuts import render

posts = [
    {
        'author': 'Zno',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 7, 2022'
    },
    {
        'author': 'Able',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 8, 2022'
    }
]


def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def support(request):
    return render(request, 'blog/support.html', {'title': 'Support'})
""" blog -> templates -> blog -> template.html """

