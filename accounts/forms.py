# -*- coding: utf-8 -*-
from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext as _

class StudentRegistrationForm(RegistrationFormUniqueEmail):
    """The form displayed for account registration, includes fields for user profile"""
    first_name = forms.CharField(label=_(u"First name"), max_length=120)
    last_name = forms.CharField(label=_(u"Last name"), max_length=120)
    # TODO: get from db
    department_choices = (
        (u"ΕΜΠ ΗΜΜΥ", u"ΕΜΠ ΗΜΜΥ"),
        (u"ΕΜΠ ΣΕΜΦΕ", u"ΕΜΠ ΣΕΜΦΕ"),
        (u"ΜΠΛΑ", u"ΜΠΛΑ"),
        (u"Άλλο", u"Άλλο"),
    )
    department = forms.ChoiceField(label=_(u"Department"), choices=department_choices)
    student_id = forms.CharField(label=_(u"Student id"), max_length=120)
