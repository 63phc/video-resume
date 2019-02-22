from django.views.generic import DetailView

from .models import Vacancy


class VacancyDetail(DetailView):
    template_name = 'vacancy/vacancy_detail.html'
    model = Vacancy
