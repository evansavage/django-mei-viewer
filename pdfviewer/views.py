import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse

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
    comments = score.score_comments_set.order_by('-date')
    template = loader.get_template('pdfviewer/index.html')
    context = {
        'score': score,
        'comments': comments
    }
    return HttpResponse(template.render(context, request))


def submit(request, score_id):
    scoreG = Score.objects.get(pk=score_id) # get_object_or_404
    # scoreG.comment_set.create(
    #     date=
    #     author=
    #     text=
    # )

    # template = loader.get_template('pdfviewer/index.html')
    comment = Score_Comments.objects.create(date=timezone.now(),score=scoreG)
    #comment.score = score_id
    comment.author = request.POST['usrname']
    comment.text = request.POST['comment']
    #comment.date = timezone.now()
    comment.save()
    #context = {}
    #return 1
    return HttpResponseRedirect(reverse('index',args=(scoreG.id,)))
