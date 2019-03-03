from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import AccountHr


class HRDashboardView(LoginRequiredMixin, TemplateView):
    model = AccountHr
    template_name = 'dashboard_hr/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HRDashboardView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(account_hr)
        return context