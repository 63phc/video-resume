import json

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, CreateView, ListView

from src.apps.question.models import Question
from src.apps.vacancy.models import Vacancy
from .models import AccountHr


class DashboardView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            account_hr__user_id=self.request.user.id
        )[:5]
        context['questions'] = Question.objects.filter(
            account_hr=self.request.user.id
        )[:5]
        return context


class DashboardVacancyListView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/vacancies.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardVacancyListView, self).get_context_data(**kwargs)
        context['object_list'] = Vacancy.objects.filter(
            account_hr__user_id=self.request.user.id
        )
        return context
