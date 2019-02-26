from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from src.apps.resume.models import Resume, Skill

from ..forms import SkillForm

from .mixins import EduSkillJobSuccessUrlMixin, ResumeEduSkillJobContextMixin


class SkillAjaxMixin:
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax():
            if request.POST['tag'] == 'create':
                form = SkillForm()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            elif request.POST['tag'] == 'add':
                form = SkillForm(request.POST)
                if form.is_valid():
                    form.save()
                    response_dict = {
                        'id': form.instance.pk,
                        'name': form.instance.name
                    }
                    return JsonResponse(response_dict)
        return super(SkillAjaxMixin, self).post(request, **kwargs)


class SkillUpdateView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, UpdateView
):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/skill/update.html'


class SkillDeleteView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin, DeleteView
):
    model = Skill
    template_name = 'dashboard_worker/skill/delete.html'


class SkillCreateView(
    ResumeEduSkillJobContextMixin, EduSkillJobSuccessUrlMixin,
    SkillAjaxMixin, CreateView
):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/skill/create.html'

    def form_valid(self, form, **kwargs):
        response = super(SkillCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))
        resume.skill.add(obj)
        resume.save()
        return response
