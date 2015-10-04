# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CryptoAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=u"Όνομα χρήστη", max_length=75)
    password = forms.CharField(label=u"Κωδικός", widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': "Ο κωδικός ή το όνομα χρήστη δεν είναι σωστός. Προσπάθησε ξανά.",
        'inactive': "Αυτός ο λογαριασμός είναι απενεργοποιημένος."
    }
