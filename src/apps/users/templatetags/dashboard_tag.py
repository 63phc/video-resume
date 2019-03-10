from django import template
from django.contrib.auth import get_user_model


User = get_user_model()
register = template.Library()


@register.simple_tag(name='dashboard_tag', takes_context=True)
def url_dashboard(context):
    user = User.objects.filter(username=context['user']).first()
    if not user:
        return context
    worker = user.workers_related.all().first()

    if worker and not context.get('worker_pk'):

        context['worker_pk'] = worker.pk

    return context
