from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# from src.apps.answer.models import Answer
from src.apps.question.models import Answer
from src.apps.vacancy.models import Vacancy
from .models import AccountHr


class DashboardView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            account_hr__user_id=self.request.user.id
        )[:5]
        context['answers'] = Answer.objects.filter(
            question__account_hr__user_id=self.request.user.id
        )[:5]
        return context


class DashboardVacancyListView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/vacancy/list.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardVacancyListView, self).get_context_data(**kwargs)
        context['object_list'] = Vacancy.objects.filter(
            account_hr__user_id=self.request.user.id
        )
        return context


class DashboardAnswerListView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/answer/list.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardAnswerListView, self).get_context_data(**kwargs)
        context['object_list'] = Answer.objects.filter(
            question__account_hr__user_id=self.request.user.id
        )
        return context
