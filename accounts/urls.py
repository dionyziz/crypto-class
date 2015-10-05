"""accounts urls configuration"""
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from registration.backends.simple.views import RegistrationView
from .views import StudentRegistrationView
from .forms import StudentRegistrationForm

urlpatterns = [
    url(r'^register/complete/', RedirectView.as_view(url='/exercises', permanent=True), name='registration_complete'),
    url(r'register', StudentRegistrationView.as_view(), name='registration_register'),
    url(r'logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^', include('registration.backends.simple.urls')),
    url(r'^', include('django.contrib.auth.urls')),
]
