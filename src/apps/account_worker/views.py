from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import Http404
from .models import AccountWorker
from src.apps.resume.models import Resume, Education, Skill, Job
from .forms import ResumeUpdateForm, EducationCreateUpdateForm, SkillCreateUpdateForm, JobCreateUpdateForm

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

    def get_context_data(self, **kwargs):
        context = super(ResumeUpdateView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        title = Resume.objects.get(pk=self.kwargs['pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('dashboard_worker:dashboard_worker_resume', kwargs={'pk': self.kwargs['w_pk']})


class EducationUpdateView(UpdateView):
    form_class = EducationCreateUpdateForm
    model = Education
    template_name = 'dashboard_worker/dashboard_education_update.html'

    def get_context_data(self, **kwargs):
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class EducationCreateView(CreateView):
    form_class = EducationCreateUpdateForm
    model = Education
    template_name = 'dashboard_worker/dashboard_education_create.html'

    def get_context_data(self, **kwargs):
        context = super(EducationCreateView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def form_valid(self, form, **kwargs):
        response = super(EducationCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = Resume.objects.get(pk=self.kwargs['res_pk'])
        resume.education.add(obj)
        resume.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class EducationDeleteView(DeleteView):
    model = Education
    template_name = 'dashboard_worker/dashboard_education_delete.html'

    def get_context_data(self, **kwargs):
        context = super(EducationDeleteView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class SkillUpdateView(UpdateView):
    form_class = SkillCreateUpdateForm
    model = Skill
    template_name = 'dashboard_worker/dashboard_skill_update.html'

    def get_context_data(self, **kwargs):
        context = super(SkillUpdateView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'dashboard_worker/dashboard_skill_delete.html'

    def get_context_data(self, **kwargs):
        context = super(SkillDeleteView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class SkillCreateView(CreateView):
    form_class = SkillCreateUpdateForm
    model = Skill
    template_name = 'dashboard_worker/dashboard_skill_create.html'

    def get_context_data(self, **kwargs):
        context = super(SkillCreateView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def form_valid(self, form, **kwargs):
        response = super(SkillCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = Resume.objects.get(pk=self.kwargs['res_pk'])
        resume.skill.add(obj)
        resume.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class JobCreateView(CreateView):
    form_class = JobCreateUpdateForm
    model = Job
    template_name = 'dashboard_worker/dashboard_job_create.html'

    def get_context_data(self, **kwargs):
        context = super(JobCreateView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def form_valid(self, form, **kwargs):
        response = super(JobCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = Resume.objects.get(pk=self.kwargs['res_pk'])
        resume.job.add(obj)
        resume.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class JobUpdateView(UpdateView):
    form_class = JobCreateUpdateForm
    model = Job
    template_name = 'dashboard_worker/dashboard_job_update.html'

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'dashboard_worker/dashboard_job_delete.html'

    def get_context_data(self, **kwargs):
        context = super(JobDeleteView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['res_pk']
        title = Resume.objects.get(pk=self.kwargs['res_pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs['res_pk'], 'w_pk': self.kwargs['w_pk']}
        )
