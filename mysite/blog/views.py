from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.template import Template, Context
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

def index(request):
    template = loader.get_template('blog/index.html')
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':last_question_list
    }
    return HttpResponse(template.render(context, request))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'blog/results.html',{'question':question})

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'blog/detail.html',{
        'question':question,
        'error_message':'You did\'n select a choice.',
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'