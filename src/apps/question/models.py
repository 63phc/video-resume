from django.db import models
from django.utils.translation import ugettext_lazy as _

from src.apps.account_hr.models import AccountHr


class Question(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    answer = models.TextField(_('Answer'), blank=True, null=True)
    account_hr = models.ManyToManyField(AccountHr, related_name='questions',
                                    verbose_name=_('Questions'), blank=True)
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return f'{self.title} - {self.account_hr.name}'