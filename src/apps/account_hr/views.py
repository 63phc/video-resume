from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# from src.apps.answer.models import Answer
from src.apps.question.models import Answer, Question
from src.apps.resume.models import Resume
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
        context['answers'] = Answer.objects.filter(
            question__account_hr__user_id=self.request.user.id
        )[:5]
        return context


class DashboardVacancyListView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/vacancy/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardVacancyListView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            account_hr__user_id=self.request.user.id
        )
        return context


class DashboardAnswerListView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/answer/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardAnswerListView, self).get_context_data(**kwargs)
        context['object_list'] = Answer.objects.filter(
            question__account_hr__user_id=self.request.user.id
        )
        return context


class DashboardResumeListView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/resume/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardResumeListView, self).get_context_data(**kwargs)
        context['object_list'] = Resume.objects.all()
        return context


class DashboardResumeDetailView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/resume/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardResumeDetailView, self).get_context_data(**kwargs)
        context['object'] = Resume.objects.get(id=kwargs['pk'])
        return context


class DashboardVacancyDetailView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/vacancy/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardVacancyDetailView, self).get_context_data(**kwargs)
        vacancy = Vacancy.objects.get(id=kwargs['pk'])
        context['object'] = vacancy
        context['questions'] = Question.objects.filter(vacancy=vacancy)
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('dashboard_hr:main')
