from django import template

from src.apps.question.models import Question

register = template.Library()


@register.inclusion_tag('components/last_questions.html')
def last_questions(context):
    return {'questions': list(Question.objects.filter(
        account_hr__user=context['user'].id
    ).values(
        'id', 'title', 'text'
    ))}
