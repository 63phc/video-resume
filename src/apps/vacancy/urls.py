from django.urls import path

from .views import VacancyDetail

app_name = 'vacancy'

urlpatterns = [
    path('vacancy_detail/<int:pk>/',
         VacancyDetail.as_view(), name='vacancy_detail'),
]
