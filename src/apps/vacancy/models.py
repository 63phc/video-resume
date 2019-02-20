from django.db import models
from django.utils.translation import ugettext_lazy as _

from src.apps.account_hr.models import AccountHr


class Tag(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=70)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    account_hr = models.ManyToManyField(AccountHr, related_name='vacancies',
                                  verbose_name=_('HRs'))
    tags = models.ManyToManyField(Tag, related_name='vacancies',
                                  verbose_name=_('Tags'))

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.title
