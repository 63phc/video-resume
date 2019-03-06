from django.db import models
from django.utils.translation import ugettext_lazy as _
from src.core.utils.choices import AccountTypeChoices
from django.conf import settings
from django.urls import reverse_lazy


class AccountHr(models.Model):
    """ Class model for hr """

    type_account = models.CharField(
        _('Type user'), choices=AccountTypeChoices.CHOICES, max_length=63
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_('HR'), related_name='hrs_related')

    class Meta:
        verbose_name = _('Account hr')
        verbose_name_plural = _('Account hrs')

    def __str__(self):
        return f'{self.user.username} - {self.type_account}'

    def get_absolute_url(self):
        return reverse_lazy('dashboard_hr')
