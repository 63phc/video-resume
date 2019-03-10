from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from django.conf import settings

from src.core.utils.choices import AccountTypeChoices
from src.apps.resume.models import Resume


class WorkerCheckingQuerySet(models.QuerySet):
    def is_created(self):
        return self.all().first()


class AccountWorker(models.Model):
    """ Class model for workers """

    type_account = models.CharField(
        _('Type user'), choices=AccountTypeChoices.CHOICES, max_length=63
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_('workers'), related_name='workers_related')
    resume = models.ManyToManyField(
        Resume,
        related_name='resumes',
        verbose_name=_('Resume'),
        blank=True
    )
    objects = WorkerCheckingQuerySet.as_manager()

    class Meta:
        verbose_name = _('Account worker')
        verbose_name_plural = _('Account workers')

    def __str__(self):
        return f'{self.user.username} - {self.type_account}'

    @property
    def get_absolute_url(self):
        return reverse_lazy(
            'dashboard_worker:dashboard_worker_main', kwargs={'pk': self.pk})
