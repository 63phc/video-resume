from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse

from src.apps.resume.models import Resume, Education

from ..forms import EducationForm


class EducationAjaxMixin:
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if request.POST['tag'] == 'create':
                form = EducationForm()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            elif request.POST['tag'] == 'add':
                form = EducationForm(request.POST)
                if form.is_valid():
                    form.save()
                    response_dict = {
                        'pk': form.instance.pk,
                        'name_institution': form.instance.name_institution
                    }
                    return JsonResponse(response_dict)
        return super(EducationAjaxMixin, self).post(request, **kwargs)


class EducationUpdateView(UpdateView):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/dashboard_education_update.html'

    def get_context_data(self, **kwargs):
        context = super(EducationUpdateView, self).get_context_data(**kwargs)
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


class EducationCreateView(EducationAjaxMixin, CreateView):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/dashboard_education_create.html'

    def get_context_data(self, **kwargs):
        context = super(EducationCreateView, self).get_context_data(**kwargs)
        context['resume_pk'] = self.kwargs.get('resume_pk')
        title = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        context['title'] = title.title
        context['w_pk'] = self.kwargs.get('w_pk')
        return context

    def form_valid(self, form, **kwargs):
        response = super(EducationCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        resume.education.add(obj)
        resume.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs.get('resume_pk'), 'w_pk': self.kwargs.get('w_pk')}
        )


class EducationDeleteView(DeleteView):
    model = Education
    template_name = 'dashboard_worker/dashboard_education_delete.html'

    def get_context_data(self, **kwargs):
        context = super(EducationDeleteView, self).get_context_data(**kwargs)
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
