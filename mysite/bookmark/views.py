from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.context_processors import request
from django.views.generic import ListView, DetailView

from bookmark.models import BookMark


def BookMarkLV(request):
    bookmarks = BookMark.objects.all()
    return render(request, 'bookmark_list.html', {"bookmarkList" : bookmarks})


def BookMarkDV(request, num):
    bookmarkdetail = BookMark.objects.get(id=num)
    return render(request, 'bookmark_detail.html', {"bookmark" : bookmarkdetail})