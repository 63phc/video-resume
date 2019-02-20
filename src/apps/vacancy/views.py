from django.views.generic import DetailView
from django.shortcuts import render

from src.apps.vacancy.models import Vacancy


class VacancyDetail(DetailView):
    template_name = 'vacancy/vacancy_detail.html'
    model = Vacancy
