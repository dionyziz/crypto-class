# -*- coding: utf8 -*-

from django import forms

class DocumentForm(forms.Form):
    pdf_file = forms.FileField(
        label=u'PDF αρχείο: ',
        help_text=u'Μέγιστο μεγεθος: 10ΜΒ'
    )

class TextAnswerForm(forms.Form):
    answer = forms.CharField(label=u'Απάντηση')

