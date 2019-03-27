from django.urls import path

from .views import VacancyDetailView, VacancyCreateView, tag_create_view, \
    VacancyListView

app_name = 'vacancy'

urlpatterns = [
    path('detail/<int:pk>/',
         VacancyDetailView.as_view(), name='detail'),
    path('create/',
         VacancyCreateView.as_view(), name='create'),
    path('list/',
         VacancyListView.as_view(), name='list'),
]
