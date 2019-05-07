import datetime

from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
=======
from django.http import HttpResponse
from django.http import HttpResponseRedirect
>>>>>>> 2ee6c83771d419334f06298e766424aa6e7a1f48
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
<<<<<<< HEAD
=======

>>>>>>> 2ee6c83771d419334f06298e766424aa6e7a1f48

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
    scoreG = Score.objects.get(pk=score_id)
    # template = loader.get_template('pdfviewer/index.html')
<<<<<<< HEAD
    comment = Score_Comments.objects.create(date=timezone.now(), score=scoreG)
    comment.author = request.POST['usrname']
    comment.text = request.POST['comment']
    # comment.date = timezone.now()
    comment.save()
    context = {}
    return HttpResponseRedirect(reverse(f'pdfviewer:submit', args=(scoreG.id)))
    # return HttpResponseRedirect(reverse('pdfviewer:' + score_id), args=(score.id,))
=======
    comment = Score_Comments.objects.create(date=timezone.now(),score=scoreG)
    #comment.score = score_id
    comment.author = request.POST['usrname']
    comment.text = request.POST['comment']
    #comment.date = timezone.now()
    comment.save()
    context = {}
    #return 1
    return HttpResponseRedirect(reverse('index',args=(scoreG.id,)))
>>>>>>> 2ee6c83771d419334f06298e766424aa6e7a1f48
