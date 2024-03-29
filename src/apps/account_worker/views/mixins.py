from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from django.contrib.auth import get_user_model

from src.apps.resume.models import Resume
from src.apps.question.models import Question
from ..models import WorkerAnswered


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
                    if self.form_class.__name__ == 'AnswerForm':
                        form.save(commit=False)
                        form.instance.question = get_object_or_404(Question, pk=self.request.POST['question'])
                        form.save()
                        user = get_object_or_404(User, pk=self.request.user.pk)
                        worker = user.workers.is_created(user=user)
                        if user.workers.is_created(user=user).answer.filter(
                                question=form.instance.question.pk).first():
                            answer = user.workers.is_created(user=user).answer.get(
                                question=form.instance.question.pk)
                            user.workers.is_created(user=user).answer.remove(answer)
                            answer.delete()
                        user.workers.is_created(user=user).answer.add(form.instance)
                        form.save()
                        answered = WorkerAnswered.objects.create(
                            worker=worker, question=form.instance.question,
                            answer=form.instance)
                        answered.save()
                        response_dict = {'response': form.instance.answer}
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


def worker_access(function):
    def wrapper(request, *args, **kwargs):
        if request.is_ajax():
            return function(request, *args, **kwargs)

        user = get_object_or_404(User, username=request.user)
        worker = user.workers.is_created(user=user)
        pk = kwargs.get('worker_pk') or kwargs.get('pk')
        if worker.pk != int(pk):
            raise Http404

        return function(request, *args, **kwargs)

    return wrapper


class QuestionContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(
            QuestionContextMixin, self).get_context_data(**kwargs)
        context['worker_pk'] = self.kwargs.get('worker_pk')
        return context
