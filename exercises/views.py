# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'user': request.user}
    return render(request, 'exercises/index.html', context)
