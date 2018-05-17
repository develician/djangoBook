from django.conf.urls import url

from blog.views import PostLV

urlpatterns = [
    url(r'^$', PostLV, name='index')
]