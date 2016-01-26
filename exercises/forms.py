# -*- coding: utf8 -*-
from django import forms
from django.forms import widgets

from captcha.fields import ReCaptchaField

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label=u'Επιλογή αρχείου PDF/DOC/ODF:',
        help_text=u'Μέγιστο μεγεθος αρχείου: 10ΜΒ'
    )

    captcha = ReCaptchaField(label='')

class TextAnswerForm(forms.Form):
    answer = forms.CharField(
                    label=u'Απάντηση',
                    widget=widgets.Textarea(attrs={'rows': 1 })
                    )

    captcha = ReCaptchaField(label='')
