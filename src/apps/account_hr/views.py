from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import AccountHr


class HRDashboardView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HRDashboardView, self).get_context_data(**kwargs)
        context['vacancies'] = [
            {'title': 'Vacancy Number 1', 'description': 'descr for vac #1'},
            {'title': 'Vacancy Number 2', 'description': 'descr for vac #2'},
            {'title': 'Vacancy Number 3', 'description': 'descr for vac #3'},
        ]
        # Vacancy.objects.filter(account_hr)
        return context