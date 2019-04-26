from django.urls import path

from ..views import QuestionsListView, QuestionDetailView, AnswerAddSubmitForm


app_name = 'dashboard_worker'


urlpatterns = [
    path(
        'questions/<worker_pk>', QuestionsListView.as_view(),
        name='dashboard_worker_question'),
    path(
        'questions/detail/<pk>/<worker_pk>', QuestionDetailView.as_view(),
        name='dashboard_worker_question_detail'),
    path(
        'questions/detail/answer/', AnswerAddSubmitForm.as_view(),
        name='dashboard_worker_question_answer'),
]
