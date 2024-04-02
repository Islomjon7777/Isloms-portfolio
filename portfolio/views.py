from django.shortcuts import render
from .models import PostModel
def index(request):
    posts = PostModel.objects.all()

    ctx = {
        'posts': posts
    }
    return render(request, 'index.html', ctx)

