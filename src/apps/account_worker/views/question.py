from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from src.apps.question.models import Question, Answer
from ..forms import AnswerForm
from .mixins import (
    worker_access, QuestionContextMixin, EduSkillJobAjaxMixin)


@method_decorator((login_required, worker_access), name='dispatch')
class QuestionsListView(QuestionContextMixin, ListView):
    model = Question
    template_name = 'dashboard_worker/question/list.html'

    def get_queryset(self, **kwargs):
        questions = Question.objects.exclude(
            answered_questions__worker__pk=self.kwargs.get('worker_pk'))
        return questions

    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data()
        context['answered'] = Question.objects.filter(
            answered_questions__worker__pk=self.kwargs.get('worker_pk'))
        return context


@method_decorator((login_required, worker_access), name='dispatch')
class QuestionDetailView(QuestionContextMixin, DetailView):
    model = Question
    template_name = 'dashboard_worker/question/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        answer = Answer.objects.is_worker_answered(
            question=question, worker_pk=self.kwargs.get('worker_pk'))
        if answer:
            context['worker_answer'] = answer.answer

        return context


@method_decorator((login_required, worker_access), name='dispatch')
class AnswerAddSubmitForm(EduSkillJobAjaxMixin, CreateView):
    form_class = AnswerForm
    model = Answer
