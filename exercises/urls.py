from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bonus/(?P<secret>[a-zA-Z0-9]+)$', views.bonuslink),
    url(r'^exercises/$', views.index, name='exercise_index'),
    url(r'^$', views.homepage, name='homepage'),
]
