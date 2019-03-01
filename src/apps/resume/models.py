from unidecode import unidecode

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Education(models.Model):
    """ class education for resume(MTM) """

    period_edu = models.CharField(_('Period education'), max_length=50)
    name_institution = models.CharField(
        _('Name of institution'), max_length=100)
    faculty = models.CharField(_('Faculty'), max_length=100)
    form_study = models.CharField(_('Form of study'), max_length=30)

    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')

    def __str__(self):
        return self.name_institution


class Skill(models.Model):
    """ class skill for resume(MTM) """

    name = models.CharField(_('Name'), max_length=30)

    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')

    def __str__(self):
        return self.name


class Job(models.Model):
    """ class job for resume(MTM) """

    period_work = models.CharField(_('Period of work'), max_length=50)
    position = models.CharField(_('Position'), max_length=100)
    name_company = models.CharField(_('Company name'), max_length=100)

    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    def __str__(self):
        return self.name_company


class Resume(models.Model):
    """ class resume for worker(MTM) """

    title = models.CharField(_('Title'), max_length=100, default='')
    other_skills = models.CharField(
        _('Other skills'), max_length=200, default='')
    hobbies = models.CharField(_('Hobbies'), max_length=200, default='')
    about = models.CharField(_('About'), max_length=400, default='')
    education = models.ManyToManyField(
        Education,
        related_name='educations',
        verbose_name=_('Education'),
    )
    skill = models.ManyToManyField(
        Skill,
        related_name='skills',
        verbose_name=_('Skills'),
    )
    job = models.ManyToManyField(
        Job,
        related_name='jobs',
        verbose_name=_('Jobs'),
    )
    slug = models.SlugField(_('Slug'), max_length=100, allow_unicode=True)
    created_at = models.DateTimeField(
        verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_('Updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('resume')
        verbose_name_plural = _('resumes')

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Resume, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def educations(self):
        return ", ".join(
            [row.name_institution for row in self.education.all()]
        )

    @property
    def skills(self):
        return ", ".join([row.name for row in self.skill.all()])

    @property
    def jobs(self):
        return ", ".join([row.name_company for row in self.job.all()])


@receiver(pre_delete, sender=Resume)
def pre_delete_story(sender, instance, **kwargs):
    for edu in instance.education.all():
        edu.delete()
    for skill in instance.skill.all():
        skill.delete()
    for job in instance.job.all():
        job.delete()
