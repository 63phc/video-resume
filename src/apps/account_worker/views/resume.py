from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from src.apps.account_worker.models import AccountWorker
from src.apps.resume.models import Resume
from src.apps.account_worker.forms import ResumeMainForm, ResumeForm
from .mixins import ResumeEduSkillJobContextMixin, worker_access

User = get_user_model()


class ResumeSuccessUrlMixin:
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume',
            kwargs={'pk': self.kwargs.get('worker_pk')}
        )


@method_decorator((login_required, worker_access), name='dispatch')
class AccountWorkerView(DetailView):
    model = AccountWorker
    template_name = 'dashboard_worker/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AccountWorkerView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context


@method_decorator((login_required, worker_access), name='dispatch')
class ResumeListView(ListView):
    model = AccountWorker
    template_name = 'dashboard_worker/resume/list.html'

    def get_queryset(self, **kwargs):
        query = get_object_or_404(AccountWorker, pk=self.kwargs.get('pk'))
        return query.resume.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context


@method_decorator((login_required, worker_access), name='dispatch')
class ResumeCreateView(ResumeSuccessUrlMixin, CreateView):
    model = Resume
    form_class = ResumeMainForm
    template_name = 'dashboard_worker/resume/create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['worker_pk'] = self.kwargs.get('worker_pk')
        return context

    def form_invalid(self, form, **kwargs):
        form_fix = ResumeForm(self.request.POST)
        if form_fix.is_valid():
            obj = form_fix.save()
            account = get_object_or_404(
                AccountWorker, pk=self.kwargs.get('worker_pk')
            )
            account.resume.add(obj)
            account.save()
            return HttpResponseRedirect(self.get_success_url())
        return super(
            ResumeCreateView, self).form_invalid(form)

    def form_valid(self, form, **kwargs):
        response = super(ResumeCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        account = get_object_or_404(
            AccountWorker, pk=self.kwargs.get('worker_pk')
        )
        account.resume.add(obj)
        account.save()
        return response


@method_decorator((login_required, worker_access), name='dispatch')
class ResumeUpdateView(ResumeEduSkillJobContextMixin,
                       ResumeSuccessUrlMixin, UpdateView):
    form_class = ResumeMainForm
    model = Resume
    template_name = 'dashboard_worker/resume/update.html'


@method_decorator((login_required, worker_access), name='dispatch')
class ResumeDeleteView(ResumeEduSkillJobContextMixin,
                       ResumeSuccessUrlMixin, DeleteView):
    model = Resume
    template_name = 'dashboard_worker/resume/delete.html'
