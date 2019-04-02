from django import template

from src.apps.resume.models import Resume

register = template.Library()


@register.inclusion_tag('components/last_resumes.html')
def last_resumes():
    return {'resumes': list(Resume.objects.values('id', 'title', 'about'))}
