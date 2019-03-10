from django.db import models
from django.utils.translation import ugettext_lazy as _
from src.core.utils.choices import AccountTypeChoices


class AccountHr(models.Model):
    """ Class model for hr """

    type_account = models.CharField(
        _('Type user'), choices=AccountTypeChoices.CHOICES, max_length=63
    )
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Account hr')
        verbose_name_plural = _('Account hrs')

    def __str__(self):
        return f'{self.user.username} - {self.type_account}'
