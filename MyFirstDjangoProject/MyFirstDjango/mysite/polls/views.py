from lib2to3.fixes.fix_input import context
from urllib.request import parse_keqv_list

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Survey, Question


# Create your views here.
def index(request):
    question_list = Question.objects.all()
    context = {
        "questions": question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice_radios"])
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    except (KeyError, Choice.DoesNotExist):
        error_context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }
        return render(request, "polls/detail.html", error_context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question
    }
    return render(request, "polls/results.html", context)


# Display all surveys
@login_required
def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'polls/survey_list.html', {'surveys': surveys})

# Display details of a single survey and its questions
@login_required
def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.questions.all()
    return render(request, 'polls/survey_detail.html', {'survey': survey, 'questions': questions})












