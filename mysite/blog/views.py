from django.shortcuts import render

# Create your views here.
from blog.models import Post


def PostLV(request):
    posts = Post.objects.all()
    return render(request, 'post_all.html', {"posts" : posts})