from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView
from .serializers import *


# Create your views here.
class ApiQuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choice_set.get(pk=request.POST['choice'])

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect('result')