import json

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, CreateView

from src.apps.vacancy.models import Vacancy
from .models import AccountHr


class DashboardView(LoginRequiredMixin, DetailView):
    model = AccountHr
    template_name = 'dashboard_hr/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            account_hr=self.object.id
        )[:5]
        return context


class AccountHrCreateView(CreateView):
    model = AccountHr
    fields = ['user', 'type_account', ]
    template_name = 'dashboard_hr/parts/create_hr.html'
    success_url = ''
