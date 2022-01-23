from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Luis",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "January 23, 2022",
    },
    {
        "author": "Tom",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "January 23, 2022",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
