from django.urls import path

from .views import VacancyDetail, VacancyCreateView, tag_create_view

app_name = 'vacancy'

urlpatterns = [
    path('detail/<int:pk>/',
         VacancyDetail.as_view(), name='vacancy_detail'),
    path('create/',
         VacancyCreateView.as_view(), name='vacancy_create'),
]
