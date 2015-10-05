from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^exercises/$', views.index, name='exercise_index'),
    url(r'^$', views.homepage, name='homepage'),
]
