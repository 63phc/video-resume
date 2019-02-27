from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from src.apps.account_hr.models import AccountHr


class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=70)
    slug = models.SlugField(_('Slug'), max_length=256, unique=True)
    is_activated = models.BooleanField(_('Activated'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        else:
            self.slug = slugify(self.slug, allow_unicode=True)
        super(Tag, self).save()


class Vacancy(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    account_hr = models.ManyToManyField(AccountHr,
        related_name='vacancies',verbose_name=_('HRs'))
    tags = models.ManyToManyField(Tag, related_name='vacancies',
                                  verbose_name=_('Tags'))
    slug = models.SlugField(_('Slug'), max_length=256, unique=True)
    is_activated = models.BooleanField(_('Activated'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        else:
            self.slug = slugify(self.slug, allow_unicode=True)
        super(Vacancy, self).save()