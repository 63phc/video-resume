from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import Http404
from .models import AccountWorker
from src.apps.resume.models import Resume, Education, Skill, Job
from .forms import (
    ResumeCreateUpdateForm,
    EducationCreateUpdateForm,
    SkillCreateUpdateForm,
    JobCreateUpdateForm
)
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import ResumeForm

User = get_user_model()


class AccountWorkerView(DetailView):
    model = AccountWorker

    def get_template_names(self):
        user = User.objects.filter(username=self.request.user)
        if len(user) != 1:
            raise Http404
        return ['dashboard_worker/dashboard_worker.html']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AccountWorkerView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


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


class ResumeCreateView(CreateView):
    model = Resume
    form_class = ResumeCreateUpdateForm
    template_name = 'dashboard_worker/dashboard_resume_create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def form_invalid(self, form, **kwargs):
        pre_form = ResumeForm(self.request.POST)
        if pre_form.is_valid():
            obj = pre_form.save()
            account = AccountWorker.objects.get(pk=self.kwargs['w_pk'])
            account.resume.add(obj)
            account.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(ResumeCreateView, self).form_invalid(form, **kwargs)

    def form_valid(self, form, **kwargs):
        response = super(ResumeCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        account = AccountWorker.objects.get(pk=self.kwargs['w_pk'])
        account.resume.add(obj)
        account.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume',
            kwargs={'pk': self.kwargs['w_pk']}
        )


class ResumeUpdateView(UpdateView):
    form_class = ResumeCreateUpdateForm
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
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume',
            kwargs={'pk': self.kwargs['w_pk']}
        )


class ResumeDeleteView(DeleteView):
    model = Resume
    template_name = 'dashboard_worker/dashboard_resume_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeDeleteView, self).get_context_data(**kwargs)
        context['res_pk'] = self.kwargs['pk']
        title = Resume.objects.get(pk=self.kwargs['pk'])
        context['title'] = title.title
        context['w_pk'] = self.kwargs['w_pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume',
            kwargs={'pk': self.kwargs['w_pk']}
        )


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

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if request.POST['tag'] == 'create':
                form = EducationCreateUpdateForm()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            elif request.POST['tag'] == 'add':
                form = EducationCreateUpdateForm(request.POST)
                if form.is_valid():
                    form.save()
                    response_dict = {
                        'pk': form.instance.pk,
                        'name_institution': form.instance.name_institution
                    }
                    return JsonResponse(response_dict)
        return super(EducationCreateView, self).post(request, **kwargs)

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

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if request.POST['tag'] == 'create':
                form = SkillCreateUpdateForm()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            elif request.POST['tag'] == 'add':
                form = SkillCreateUpdateForm(request.POST)
                if form.is_valid():
                    form.save()
                    response_dict = {
                        'pk': form.instance.pk,
                        'name': form.instance.name
                    }
                    return JsonResponse(response_dict)
        return super(SkillCreateView, self).post(request, **kwargs)

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

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if request.POST['tag'] == 'create':
                form = JobCreateUpdateForm()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            elif request.POST['tag'] == 'add':
                form = JobCreateUpdateForm(request.POST)
                if form.is_valid():
                    form.save()
                    response_dict = {
                        'pk': form.instance.pk,
                        'name_company': form.instance.name_company
                    }
                    return JsonResponse(response_dict)
        return super(JobCreateView, self).post(request, **kwargs)

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
            kwargs={
                'pk': self.kwargs['res_pk'],
                'w_pk': self.kwargs['w_pk']
            }
        )
