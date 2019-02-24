from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse

from src.apps.resume.models import Resume, Skill

from ..forms import SkillForm


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
                        'pk': form.instance.pk,
                        'name': form.instance.name
                    }
                    return JsonResponse(response_dict)
        return super(SkillAjaxMixin, self).post(request, **kwargs)


class SkillUpdateView(UpdateView):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/dashboard_skill_update.html'

    def get_context_data(self, **kwargs):
        context = super(SkillUpdateView, self).get_context_data(**kwargs)
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


class SkillDeleteView(DeleteView):
    model = Skill
    template_name = 'dashboard_worker/dashboard_skill_delete.html'

    def get_context_data(self, **kwargs):
        context = super(SkillDeleteView, self).get_context_data(**kwargs)
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


class SkillCreateView(SkillAjaxMixin, CreateView):
    form_class = SkillForm
    model = Skill
    template_name = 'dashboard_worker/dashboard_skill_create.html'

    def get_context_data(self, **kwargs):
        context = super(SkillCreateView, self).get_context_data(**kwargs)
        context['resume_pk'] = self.kwargs.get('resume_pk')
        title = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        context['title'] = title.title
        context['w_pk'] = self.kwargs.get('w_pk')
        return context

    def form_valid(self, form, **kwargs):
        response = super(SkillCreateView, self).form_valid(form)
        obj = form.save(commit=False)
        resume = Resume.objects.get(pk=self.kwargs.get('resume_pk'))
        resume.skill.add(obj)
        resume.save()
        return response

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={'pk': self.kwargs.get('resume_pk'), 'w_pk': self.kwargs.get('w_pk')}
        )
