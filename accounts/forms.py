# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext as _

class StudentRegistrationForm(RegistrationFormUniqueEmail):
    department = forms.CharField(label=_(u"Department"), max_length=125)
    student_id = forms.IntegerField(label=_(u"Student id"))
