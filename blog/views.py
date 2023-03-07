from django.shortcuts import render

posts = [
    {
        'author': 'Ibtisam',
        'content': 'bubble is great',
        'date': '07/03/2023',
    },
    {
        'author': 'Ibtisam',
        'content': 'sorry to burst your bubble',
        'date': '07/03/2023',
    },
    {
        'author': 'Ibtisam',
        'content': 'we\'re in a bubble',
        'date': '07/03/2023',
    }
]

def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', context={'title': 'About'})
