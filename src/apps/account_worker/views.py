from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import Http404
from .models import AccountWorker
from src.apps.resume.models import Resume
from .forms import ResumeUpdateForm

User = get_user_model()


class AccountWorkerView(DetailView):
    model = AccountWorker
    template_name = 'dashboard_worker/dashboard_worker.html'

    def get_template_names(self):
        user = User.objects.filter(username=self.request.user)
        if len(user) != 1:
            raise Http404
        return ['dashboard_worker/dashboard_worker.html']


class ResumeListView(ListView):
    model = AccountWorker
    template_name = 'dashboard_worker/dashboard_resume.html'

    def get_queryset(self, **kwargs):
        query = AccountWorker.objects.get(pk=self.kwargs['pk'])
        return query.resume.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class ResumeUpdateView(UpdateView):
    form_class = ResumeUpdateForm
    model = Resume
    template_name = 'dashboard_worker/dashboard_resume_update.html'
    # fields = [
    #     'title',
    #     'other_skills',
    #     'hobbies',
    #     'about',
    #     'education',
    #     'skill',
    #     'job'
    # ]

    def get_context_data(self, **kwargs):
        context = super(ResumeUpdateView, self).get_context_data(**kwargs)
        worker = AccountWorker.objects.filter(resume__pk=self.kwargs['pk'])
        context['pk'] = worker[0].pk
        title = Resume.objects.get(pk=self.kwargs['pk'])
        context['title'] = title.title
        return context

    def get_success_url(self, **kwargs):
        worker = AccountWorker.objects.filter(resume__pk=self.kwargs['pk'])
        return reverse_lazy('dashboard_worker:dashboard_worker_resume', kwargs={'pk': worker[0].pk})
