from django.urls import path

from .views import AnswerListView

app_name = 'answer'

urlpatterns = [
    path('list/',
         AnswerListView.as_view(), name='list'),
]
