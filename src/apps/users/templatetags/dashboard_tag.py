from django import template
from django.contrib.auth import get_user_model


User = get_user_model()
register = template.Library()


@register.simple_tag(name='dashboard_tag', takes_context=True)
def url_dashboard(context):
    user = User.checking.is_exist(username=context['user'])

    if not user:
        return context

    worker = user.workers.is_created(user=user)
    hrs = user.hrs.exists()

    if worker and not context.get('worker_pk'):
        context['worker_pk'] = worker.pk
    elif hrs and not context.get('hr_pk'):
        context['hr'] = hrs

    return context
