from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from .forms import StudentRegistrationForm

class StudentRegistrationView(RegistrationView):
    form_class = StudentRegistrationForm
