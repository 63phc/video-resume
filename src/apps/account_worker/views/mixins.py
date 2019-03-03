from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from django.contrib.auth import get_user_model

from src.apps.resume.models import Resume
from src.apps.account_worker.models import AccountWorker
from django.contrib.auth.mixins import AccessMixin

User = get_user_model()


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


class EduSkillJobAjaxMixin:
    def form_invalid(self, form):
        if self.request.is_ajax():
            if self.request.POST['tag'] == 'create':
                form = self.form_class()
                response_dict = {'response': str(form)}
                return JsonResponse(response_dict)
            raise Http404
        else:
            return super(EduSkillJobAjaxMixin, self).form_invalid(form)

    def form_valid(self, form):
        if self.request.is_ajax():
            if self.request.POST['tag'] == 'add':
                form = self.form_class(self.request.POST)
                if form.is_valid():
                    form.save()
                    if self.form_class.__name__ == 'EducationForm':
                        response_dict = {
                            'id': form.instance.pk,
                            'name_institution': form.instance.name_institution
                        }
                    elif self.form_class.__name__ == 'SkillForm':
                        response_dict = {
                            'id': form.instance.pk,
                            'name': form.instance.name
                        }
                    elif self.form_class.__name__ == 'JobForm':
                        response_dict = {
                            'id': form.instance.pk,
                            'name_company': form.instance.name_company
                        }
                    return JsonResponse(response_dict)
            else:
                raise Http404
        obj = form.save(commit=False)
        resume = get_object_or_404(Resume, pk=self.kwargs.get('resume_pk'))
        obj.save()
        if self.form_class.__name__ == 'EducationForm':
            resume.education.add(obj)
        elif self.form_class.__name__ == 'SkillForm':
            resume.skill.add(obj)
        elif self.form_class.__name__ == 'JobForm':
            resume.job.add(obj)
        resume.save()
        return super(EduSkillJobAjaxMixin, self).form_valid(form)


class CheckAccess(AccessMixin, TemplateResponseMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return self.handle_no_permission()
        user = get_object_or_404(User, username=self.request.user)
        if self.kwargs.get('worker_pk'):
            pk = self.kwargs.get('worker_pk')
        else:
            pk = self.kwargs.get('pk')
        account = get_object_or_404(AccountWorker, pk=pk, worker=user)
        return super().dispatch(request, *args, **kwargs)
