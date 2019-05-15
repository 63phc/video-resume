from django.urls import path

from .views import DashboardView, DashboardVacancyListView, \
    DashboardAnswerListView, DashboardResumeListView, \
    DashboardResumeDetailView, DashboardVacancyDetailView

app_name = 'account_hr'

urlpatterns = [
    path('', DashboardView.as_view(), name='main'),
    path('vacancies/', DashboardVacancyListView.as_view(), name='vacancies'),
    path(
        'vacancies/<int:pk>/',
        DashboardVacancyDetailView.as_view(),
        name='vacancy_detail'
    ),
    path('answers/', DashboardAnswerListView.as_view(), name='answers'),
    path('resumes/', DashboardResumeListView.as_view(), name='resumes'),
    path(
        'resumes/<int:pk>', DashboardResumeDetailView.as_view(), name='resume'
    ),
]
