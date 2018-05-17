from django.conf.urls import url

from bookmark.views import BookMarkLV, BookMarkDV

urlpatterns = [
    url(r'^$', BookMarkLV, name='index'),
    url(r'^(\d+)', BookMarkDV, name='detail')
]
