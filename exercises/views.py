# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import SubmittableExercise

def homepage(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)

def index(request):
    exercise_list = SubmittableExercise.objects.order_by('tag')

    context = {
            'user': request.user,
            'exercise_list': exercise_list
        }
    return render(request, 'exercises/index.html', context)

def detail(request, exercise_tag):
    exercise = get_object_or_404(SubmittableExercise, tag=exercise_tag)

    #TODO: Check if user sees the exercise for the first time
    #       If so, generate the appropriate data

    context = {
            'user': request.user,
            'exercise': exercise
        }
    return render(request, 'exercises/detail.html', context)
