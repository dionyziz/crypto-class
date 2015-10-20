from django.contrib import admin
from .models import Teacher, Slide, Lecture

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Slide)
admin.site.register(Lecture)
