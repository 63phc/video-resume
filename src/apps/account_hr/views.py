from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView

from src.apps.vacancy.models import Vacancy
from .models import AccountHr


class HRDashboardView(LoginRequiredMixin, DetailView):
    model = AccountHr
    template_name = 'dashboard_hr/index.html'

    def get_context_data(self, *args, **kwargs):
        hr_id = AccountHr.objects.get(id_user=self.request.user).id
        context = super(HRDashboardView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            account_hr=self.object.id
        )[:5]
        return context