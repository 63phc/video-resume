from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from src.apps.account_worker.models import AccountWorker
from src.apps.resume.models import Resume

from src.apps.account_worker.forms import ResumeMainForm, ResumeForm

from .mixins import ResumeEduSkillJobContextMixin

User = get_user_model()


class ResumeSuccessUrlMixin:
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume',
            kwargs={'pk': self.kwargs.get('worker_pk')}
        )


class AccountWorkerView(DetailView):
    model = AccountWorker

    def get_template_names(self):
        user = get_object_or_404(User, username=self.request.user)
        return [
            'dashboard_worker/dashboard_worker.html']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AccountWorkerView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context


class ResumeListView(ListView):
    model = AccountWorker
    template_name = 'dashboard_worker/dashboard_resume.html'

    def get_queryset(self, **kwargs):
        query = get_object_or_404(AccountWorker, pk=self.kwargs.get('pk'))
        return query.resume.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context


class ResumeCreateView(ResumeSuccessUrlMixin, CreateView):
    model = Resume
    form_class = ResumeMainForm
    template_name = 'dashboard_worker/dashboard_resume_create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['worker_pk'] = self.kwargs.get('worker_pk')
        return context

    def form_invalid(self, form, **kwargs):
        form = ResumeForm(self.request.POST)
        if form.is_valid():
            obj = form.save()
            account = get_object_or_404(
                AccountWorker, pk=self.kwargs.get('worker_pk')
            )
            account.resume.add(obj)
            account.save()
            return HttpResponseRedirect(self.get_success_url())
        return super(
            ResumeCreateView, self).form_invalid(form, **kwargs)

    def form_valid(self, form, **kwargs):
        response = super(ResumeCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        account = get_object_or_404(
            AccountWorker, pk=self.kwargs.get('worker_pk')
        )
        account.resume.add(obj)
        account.save()
        return response


class ResumeUpdateView(ResumeEduSkillJobContextMixin, ResumeSuccessUrlMixin, UpdateView):
    form_class = ResumeMainForm
    model = Resume
    template_name = 'dashboard_worker/dashboard_resume_update.html'


class ResumeDeleteView(ResumeEduSkillJobContextMixin, ResumeSuccessUrlMixin, DeleteView):
    model = Resume
    template_name = 'dashboard_worker/dashboard_resume_delete.html'
