from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from src.apps.resume.models import Resume, Job

from ..forms import JobForm

from .mixins import EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin


class JobAjaxMixin:
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if request.POST['tag'] == 'create':
                form = JobForm()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            elif request.POST['tag'] == 'add':
                form = JobForm(request.POST)
                if form.is_valid():
                    form.save()
                    response_dict = {
                        'id': form.instance.pk,
                        'name_company': form.instance.name_company
                    }
                    return JsonResponse(response_dict)
        return super(JobAjaxMixin, self).post(request, **kwargs)


class JobCreateView(ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, JobAjaxMixin, CreateView):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/dashboard_job_create.html'

    def form_valid(self, form, **kwargs):
        response = super(JobCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))
        resume.job.add(obj)
        resume.save()
        return response


class JobUpdateView(ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, UpdateView):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/dashboard_job_update.html'


class JobDeleteView(ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, DeleteView):
    model = Job
    template_name = 'dashboard_worker/dashboard_job_delete.html'
