from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse

from src.apps.resume.models import Resume, Job

from ..forms import JobForm


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
                        'pk': form.instance.pk,
                        'name_company': form.instance.name_company
                    }
                    return JsonResponse(response_dict)
        return super(JobAjaxMixin, self).post(request, **kwargs)


class JobCreateView(JobAjaxMixin, CreateView):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/dashboard_job_create.html'

    def get_context_data(self, **kwargs):
        context = super(JobCreateView, self).get_context_data(**kwargs)
        context['resume_pk'] = self.kwargs.get('resume_pk')
        title = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        context['title'] = title.title
        context['w_pk'] = self.kwargs.get('w_pk')
        return context

    def form_valid(self, form, **kwargs):
        response = super(JobCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        resume.job.add(obj)
        resume.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs.get('resume_pk'), 'w_pk': self.kwargs.get('w_pk')}
        )


class JobUpdateView(UpdateView):
    form_class = JobForm
    model = Job
    template_name = 'dashboard_worker/dashboard_job_update.html'

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        context['resume_pk'] = self.kwargs.get('resume_pk')
        title = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        context['title'] = title.title
        context['w_pk'] = self.kwargs.get('w_pk')
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs.get('resume_pk'), 'w_pk': self.kwargs.get('w_pk')}
        )


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'dashboard_worker/dashboard_job_delete.html'

    def get_context_data(self, **kwargs):
        context = super(JobDeleteView, self).get_context_data(**kwargs)
        context['resume_pk'] = self.kwargs.get('resume_pk')
        title = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        context['title'] = title.title
        context['w_pk'] = self.kwargs.get('w_pk')
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={
                'pk': self.kwargs.get('resume_pk'),
                'w_pk': self.kwargs.get('w_pk')
            }
        )
