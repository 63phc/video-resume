from django.urls import path

from .views import DashboardView, DashboardVacancyListView

app_name = 'account_hr'

urlpatterns = [
    path('', DashboardView.as_view(), name='main'),
    path('vacancies/', DashboardVacancyListView.as_view(), name='vacancies'),

]
