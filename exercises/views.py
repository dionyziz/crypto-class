# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import BonusLink, BonusView, SubmittableExercise, Submission
from .forms import DocumentForm, TextAnswerForm

def homepage(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)

def index(request):
    exercise_list = SubmittableExercise.objects.order_by('tag')

    active_exercises = [ exercise for exercise in exercise_list if exercise.can_be_submitted() ]
    past_exercises = [ exercise for exercise in exercise_list if exercise not in active_exercises ]

    context = {
            'user': request.user,
            'active_exercises': active_exercises,
            'past_exercises': past_exercises,
        }
    return render(request, 'exercises/index.html', context)

def detail(request, exercise_tag):
    user = request.user
    exercise = get_object_or_404(SubmittableExercise, tag=exercise_tag)

    submissions = None
    if not user.is_anonymous() and user.is_authenticated():
        submissions = exercise.get_user_submissions(user)

    if exercise.type == exercise.AUTO_GRADING:
        if request.method == 'POST':
            form = TextAnswerForm(request.POST)

            if form.is_valid():
                answer = form.cleaned_data['answer']

                # Call grader here
                is_solution = True

                # Save submission
                submission = Submission.objects.create(
                        user=user,
                        time_submitted=timezone.now(),
                        answer=answer,
                        is_solution=is_solution
                        )
                exercise.submissions.add(submission)

                return HttpResponseRedirect(reverse('exercise_detail', kwargs={'exercise_tag': exercise_tag} ))
        else:
            form = TextAnswerForm()

    elif exercise.type == exercise.THEORETICAL:
        pass

    #TODO: Check if user sees the exercise for the first time
    #       If so, generate the appropriate data

    context = {
            'user': user,
            'exercise': exercise,
            'submissions': submissions,
            'form': form,
        }
    return render(request, 'exercises/detail.html', context)

@login_required
def bonuslink(request, secret):
    link = get_object_or_404(BonusLink, secret=secret)
    BonusView.objects.create(user=request.user, link=link)
    context = {'user': request.user, 'link': link}
    return render(request, 'exercises/bonuslink.html', context)
