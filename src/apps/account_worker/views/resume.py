from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect

from src.apps.account_worker.models import AccountWorker

from src.apps.resume.models import Resume

from src.apps.account_worker.forms import ResumeMainForm, ResumeForm


User = get_user_model()


class ResumeContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(ResumeContextMixin, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        title = Resume.objects.get(pk=self.kwargs.get('pk'))
        context['title'] = title.title
        context['w_pk'] = self.kwargs.get('w_pk')
        return context


class ResumeSuccessUrlMixin:
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume',
            kwargs={'pk': self.kwargs.get('w_pk')}
        )


class AccountWorkerView(DetailView):
    model = AccountWorker

    def get_template_names(self):
        user = User.objects.filter(username=self.request.user)
        if not user:
            raise Http404
        return \
            ['dashboard_worker/dashboard_worker.html']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AccountWorkerView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context


class ResumeListView(ListView):
    model = AccountWorker
    template_name = 'dashboard_worker/dashboard_resume.html'

    def get_queryset(self, **kwargs):
        query = AccountWorker.objects.get(pk=self.kwargs.get('pk'))
        return \
            query.resume.all()

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
        context['w_pk'] = self.kwargs.get('w_pk')
        return context

    def form_invalid(self, form, **kwargs):
        form = ResumeForm(self.request.POST)
        if form.is_valid():
            obj = form.save()
            account = AccountWorker.objects.get(pk=self.kwargs.get('w_pk'))
            account.resume.add(obj)
            account.save()
            return \
                HttpResponseRedirect(self.get_success_url())
        else:
            return \
                super(ResumeCreateView, self).form_invalid(form, **kwargs)

    def form_valid(self, form, **kwargs):
        response = super(ResumeCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        account = AccountWorker.objects.get(pk=self.kwargs.get('w_pk'))
        account.resume.add(obj)
        account.save()
        return response


class ResumeUpdateView(ResumeContextMixin, ResumeSuccessUrlMixin, UpdateView):
    form_class = ResumeMainForm
    model = Resume
    template_name = 'dashboard_worker/dashboard_resume_update.html'


class ResumeDeleteView(ResumeContextMixin, ResumeSuccessUrlMixin, DeleteView):
    model = Resume
    template_name = 'dashboard_worker/dashboard_resume_delete.html'

