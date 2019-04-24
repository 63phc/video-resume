from django.views import generic

# from src.apps.answer.models import Answer
from src.apps.question.models import Answer


class AnswerListView(generic.ListView):
    model = Answer
    template_name = 'answer/list.html'
