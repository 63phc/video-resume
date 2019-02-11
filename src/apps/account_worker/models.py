from django.db import models
from django.utils.translation import ugettext_lazy as _
from src.core.utils.choices import AccountTypeChoices
from src.apps.resume.models import Resume


class AccountWorker(models.Model):
    """ Class model for workers """

    type_account = models.CharField(
        _('Type user'), choices=AccountTypeChoices.CHOICES, max_length=63
    )
    id_user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    resume = models.ManyToManyField(Resume, related_name='resumes', verbose_name=_('Resume'))

    class Meta:
        verbose_name = _('Account worker')
        verbose_name_plural = _('Account workers')

    def __str__(self):
        return f'{self.id_user.username} - {self.type_account}'

    def number_of_resumes(self):
        count = 0
        for row in self.resume.all():
            count += 1
        return str(count)
