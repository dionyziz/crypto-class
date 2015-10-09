# -*- coding: utf8 -*-

from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label=u'Επιλογή αρχείου PDF/DOC/ODF:',
        help_text=u'Μέγιστο μεγεθος αρχείου: 10ΜΒ'
    )

class TextAnswerForm(forms.Form):
    answer = forms.CharField(label=u'Απάντηση')

