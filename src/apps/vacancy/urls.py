from django.urls import path

from src.apps.vacancy.views import VacancyDetail

app_name = 'vacancy'

urlpatterns = [
    path('vacancy_detail/<int:pk>/',
         VacancyDetail.as_view(), name='vacancy_detail'),
]
