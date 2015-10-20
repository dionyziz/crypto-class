from django import template
from django.template.defaultfilters import stringfilter
import os

register = template.Library()

@register.filter
def file_extension(file):
    return os.path.splitext(file.name)[1][1:].upper()
