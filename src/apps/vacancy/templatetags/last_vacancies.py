from django import template

from src.apps.vacancy.models import Vacancy

register = template.Library()


@register.inclusion_tag('components/last_vacancies.html')
def last_vacancies():
    return {'vacancies': list(Vacancy.objects.values('title', 'description'))}
