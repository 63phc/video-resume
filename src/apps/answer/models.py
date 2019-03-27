from django.db import models
from django.utils.translation import ugettext_lazy as _

from src.apps.account_worker.models import AccountWorker
from src.apps.question.models import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    account_worker = models.ManyToManyField(
        AccountWorker, related_name='answers', verbose_name=_('Worker'))
    text = models.TextField(_('Text'))
