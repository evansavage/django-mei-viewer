import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


# Create your views here.
from .models import Score, Score_Comments


def scores(request):
    score_list = Score.objects.order_by('title')
    template = loader.get_template('pdfviewer/scores.html')
    context = {
        'score_list': score_list
    }
    return HttpResponse(template.render(context, request))

def index(request, score_id):
    score = Score.objects.get(pk=score_id)
    template = loader.get_template('pdfviewer/index.html')
    context = {
        'score': score,
    }
    return HttpResponse(template.render(context, request))

def submit(request, score_id):
    score = Score.objects.get(pk=score_id)
    # template = loader.get_template('pdfviewer/index.html')
    comment = Score_Comments.objects.create()
    comment.score = score_id
    comment.author = request.POST['usrname']
    comment.text = request.POST['comment']
    comment.date = timezone.now()
    comment.save()
    context = {}
    return 1
    # return HttpResponseRedirect(reverse('pdfviewer:' + score_id), args=(score.id,))
