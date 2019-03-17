from django.db import models
from django.utils.translation import ugettext_lazy as _
from src.core.utils.choices import AccountTypeChoices
from django.conf import settings
from django.urls import reverse_lazy


class HrCheckingQuerySet(models.QuerySet):
    def is_created(self, user):
        return self.filter(user=user).first()


class AccountHr(models.Model):
    """ Class model for hr """

    type_account = models.CharField(
        _('Type user'), choices=AccountTypeChoices.CHOICES, max_length=63
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_('hrs'), related_name='hrs')
    objects = HrCheckingQuerySet.as_manager()

    class Meta:
        verbose_name = _('Account hr')
        verbose_name_plural = _('Account hrs')

    def __str__(self):
        return f'{self.user.username} - {self.type_account}'

    @property
    def get_absolute_url(self):
        return reverse_lazy('dashboard_hr')
