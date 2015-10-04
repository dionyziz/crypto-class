from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^exercises/$', views.index, name='index'),
    url(r'^$', views.homepage, name='homepage'),
]
