from django.shortcuts import render
from .models import Lecture

# Create your views here.
def index(request):
    lecture_list = Lecture.objects.order_by('tag')
    context = {
        'user': request.user,
        'lectures': lecture_list
    }
    return render(request, 'lectures/index.html', context)
