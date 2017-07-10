from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    template = loader.get_template('blog/index.html')
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':last_question_list
    }
    return HttpResponse(template.render(context, request))

def result(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s' % question_id)

def detail(request, question_id):
    return HttpResponse('You\'re looking at question %s.' % question_id)