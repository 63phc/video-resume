from unidecode import unidecode

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


from src.apps.account_hr.models import AccountHr


class SlugMixin(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(unidecode(self.title), allow_unicode=True)
        super(SlugMixin, self).save(force_insert, using, update_fields)


class Tag(SlugMixin, models.Model):
    is_activated = models.BooleanField(_('Activated'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title


class Vacancy(SlugMixin, models.Model):
    description = models.TextField(_('Description'))
    account_hr = models.ManyToManyField(AccountHr,
        related_name='vacancies',verbose_name=_('HRs'))
    tags = models.ManyToManyField(Tag, related_name='vacancies',
                                  verbose_name=_('Tags'))
    is_activated = models.BooleanField(_('Activated'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.title
