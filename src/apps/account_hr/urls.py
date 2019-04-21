from django.urls import path

from .views import DashboardView, DashboardVacancyListView, \
    DashboardAnswerListView

app_name = 'account_hr'

urlpatterns = [
    path('', DashboardView.as_view(), name='main'),
    path('vacancies/', DashboardVacancyListView.as_view(), name='vacancies'),
    path('answers/', DashboardAnswerListView.as_view(), name='answers'),
]
