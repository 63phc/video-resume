from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin
from django.shortcuts import get_object_or_404

from src.apps.resume.models import Resume


class EduSkillJobSuccessUrlMixin:
    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_resume_update',
            kwargs={
                'pk': self.kwargs.get('resume_pk'),
                'worker_pk': self.kwargs.get('worker_pk')
            }
        )


class ResumeEduSkillJobContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(
            ResumeEduSkillJobContextMixin, self).get_context_data(**kwargs)
        if self.kwargs.get('resume_pk'):
            context['resume_pk'] = self.kwargs.get('resume_pk')
            resume = get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))
        else:
            context['resume_pk'] = self.kwargs.get('pk')
            resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        context['title'] = resume.title
        context['worker_pk'] = self.kwargs.get('worker_pk')
        return context
