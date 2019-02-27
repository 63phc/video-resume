from django.db import models
from django.utils.translation import ugettext_lazy as _

from src.core.utils.choices import AccountTypeChoices
from src.apps.resume.models import Resume


class AccountWorker(models.Model):
    """ Class model for workers """

    type_account = models.CharField(
        _('Type user'), choices=AccountTypeChoices.CHOICES, max_length=63
    )
    worker = models.ForeignKey('users.User', on_delete=models.CASCADE)
    resume = models.ManyToManyField(
        Resume,
        related_name='resumes',
        verbose_name=_('Resume'),
        blank=True
    )

    class Meta:
        verbose_name = _('Account worker')
        verbose_name_plural = _('Account workers')

    def __str__(self):
        return f'{self.worker.username} - {self.type_account}'
