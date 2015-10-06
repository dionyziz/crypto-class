from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^exercises/$', views.index, name='exercise_index'),
    url(r'^exercises/(?P<exercise_tag>[0-9.]+)/$', views.detail, name='detail'),
    #url(r'^exercises/(?P<exercise_tag>[0-9.]+)/submit', views.submit, name='submit'),
    url(r'^bonus/(?P<secret>[a-zA-Z0-9]+)$', views.bonuslink),
    url(r'^$', views.homepage, name='homepage'),
]
