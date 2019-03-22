from django.db import models
from django.utils.translation import ugettext_lazy as _

from src.apps.account_hr.models import AccountHr


class CheckWorkerQueryset(models.QuerySet):
    def is_worker_answered(self, question, worker_pk):
        return self.filter(question=question, answers__pk=worker_pk).first()


class SetWorkerAnswered(models.QuerySet):
    def set_answered(self, worker_pk):
        all_question = self.all()
        for question in all_question:
            if question.questions.filter(question=question, answers__pk=worker_pk).first():
                question.is_answered = True
        return all_question


class SetAnsweredManager(models.Manager):
    def get_queryset(self):
        return SetWorkerAnswered(self.model, using=self._db)

    def set_answer(self, worker_pk):
        return self.get_queryset().set_answered(worker_pk)


class Question(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=256, unique=True)
    answer = models.TextField(_('Answer'), blank=True, null=True)
    account_hr = models.ManyToManyField(AccountHr, related_name='questions',
        verbose_name=_('Questions'), blank=True)
    answered = SetAnsweredManager()

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return f'{self.title} - {self.account_hr.name}'


class Answer(models.Model):
    """ class answer for worker(MTM) """

    answer = models.TextField(_('Answer'), blank=True, null=True)
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, verbose_name=_('questions'),
        related_name='questions')
    objects = CheckWorkerQueryset.as_manager()
