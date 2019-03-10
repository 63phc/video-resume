from django.urls import path

from .views import VacancyDetail, VacancyCreate, TagCreate

app_name = 'vacancy'

urlpatterns = [
    path('detail/<int:pk>/',
         VacancyDetail.as_view(), name='vacancy_detail'),
    path('create/',
         VacancyCreate.as_view(), name='vacancy_create'),
    path('create_tag/',
         TagCreate.as_view(), name='tag_create'),
]
