from django.urls import reverse_lazy
from django.views import generic

from src.apps.account_hr.models import AccountHr
from src.apps.vacancy.models import Vacancy
from .models import Question


class QuestionCreateView(generic.CreateView):
    model = Question
    template_name = 'question/create.html'
    fields = ['title', 'text', 'vacancy', 'account_hr']

    def get_success_url(self):
        return reverse_lazy('dashboard_hr:main')

    def get_initial(self):
        return {
            'account_hr': AccountHr.objects.get(user=self.request.user),
            'vacancy': Vacancy.objects.get(id=self.kwargs['vacancy_id']),
        }


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'question/detail.html'
    fields = ['title', 'text', 'vacancy']


class QuestionUpdateView(generic.UpdateView):
    model = Question
    template_name = 'question/create.html'
    fields = ['title', 'text', 'vacancy']

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['operation'] = 'update'
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('dashboard_hr:main')


class QuestionDeleteView(generic.DeleteView):
    template_name = 'vacancy/delete.html'
    model = Question
