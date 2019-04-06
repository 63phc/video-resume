from django.urls import path

from .views import VacancyDetailView, VacancyCreateView, VacancyListView, \
    VacancyUpdateView, VacancyDeleteView

app_name = 'vacancy'

urlpatterns = [
    path('detail/<int:pk>/',
         VacancyDetailView.as_view(), name='detail'),
    path('create/',
         VacancyCreateView.as_view(), name='create'),
    path('list/',
         VacancyListView.as_view(), name='list'),
    path('update/<int:pk>/',
         VacancyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',
         VacancyDeleteView.as_view(), name='delete'),
]
