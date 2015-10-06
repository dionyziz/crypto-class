# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BonusLink, BonusView

def homepage(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)

def index(request):
    context = {'user': request.user}
    return render(request, 'exercises/index.html', context)

@login_required
def bonuslink(request, secret):
    link = get_object_or_404(BonusLink, secret=secret)
    BonusView.objects.create(user=request.user, link=link)
    context = {'user': request.user, 'link': link}
    return render(request, 'exercises/bonuslink.html', context)
