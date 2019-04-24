from django.urls import path

from .views import QuestionCreateView, QuestionDetailView, QuestionUpdateView, \
    QuestionDeleteView

app_name = 'question'

urlpatterns = [
    path('create/<int:vacancy_id>/',
         QuestionCreateView.as_view(), name='create'),
    path('detail/<int:pk>/',
         QuestionDetailView.as_view(), name='detail'),
    path('update/<int:pk>/',
         QuestionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',
         QuestionDeleteView.as_view(), name='delete'),
]
