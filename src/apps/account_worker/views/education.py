from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from src.apps.resume.models import Resume, Education

from ..forms import EducationForm

from .mixins import EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin


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
                        'id': form.instance.pk,
                        'name_institution': form.instance.name_institution
                    }
                    return JsonResponse(response_dict)
        return super(EducationAjaxMixin, self).post(request, **kwargs)


class EducationUpdateView(ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, UpdateView):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/dashboard_education_update.html'


class EducationCreateView(ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, EducationAjaxMixin, CreateView):
    form_class = EducationForm
    model = Education
    template_name = 'dashboard_worker/dashboard_education_create.html'

    def form_valid(self, form, **kwargs):
        response = super(EducationCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))
        resume.education.add(obj)
        resume.save()
        return response


class EducationDeleteView(ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, DeleteView):
    model = Education
    template_name = 'dashboard_worker/dashboard_education_delete.html'
