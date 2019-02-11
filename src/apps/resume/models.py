from django.db import models
from django.utils.translation import gettext_lazy as _


class Education(models.Model):
    """ class education for resume(MTM) """

    period_edu = models.CharField(_('Period education'), max_length=50)
    name_institution = models.CharField(_('Name of institution'), max_length=100)
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

    other_skills = models.CharField(_('Other skills'), max_length=200)
    hobbies = models.CharField(_('Hobbies'), max_length=200)
    about = models.CharField(_('About'), max_length=400)
    educations = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)
    jobs = models.ManyToManyField(Job)

    class Meta:
        verbose_name = _('resume')
        verbose_name_plural = _('resumes')

    def __str__(self):
        return str(self.pk)

    def get_educations(self):
        return ", ".join([str(row.name_institution) for row in self.educations.all()])

    def get_skills(self):
        return ", ".join([str(row.name) for row in self.skills.all()])

    def get_jobs(self):
        return ", ".join([str(row.name_company) for row in self.jobs.all()])


