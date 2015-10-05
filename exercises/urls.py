from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^exercises/$', views.index, name='index'),
    url(r'^exercises/(?P<exercise_tag>[0-9.]+)/$', views.detail, name='detail'),
    #url(r'^exercises/(?P<exercise_tag>[0-9.]+)/submit', views.submit, name='submit'),
    url(r'^$', views.homepage, name='homepage'),
]
