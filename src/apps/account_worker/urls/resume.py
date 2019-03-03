from django.urls import path

from src.apps.account_worker.views import (
    AccountWorkerView, ResumeListView, ResumeUpdateView,
    ResumeCreateView, ResumeDeleteView,
)


app_name = 'dashboard_worker'

urlpatterns = [
    path('<pk>', AccountWorkerView.as_view(), name='dashboard_worker_main'),
    path(
        'resume/<pk>',
        ResumeListView.as_view(),
        name='dashboard_worker_resume'
    ),
    path(
        'resume/create/<worker_pk>',
        ResumeCreateView.as_view(),
        name='dashboard_worker_resume_create'
    ),
    path('resume/update/<pk>/<worker_pk>', ResumeUpdateView.as_view(),
         name='dashboard_worker_resume_update'),
    path('resume/delete/<pk>/<worker_pk>', ResumeDeleteView.as_view(),
         name='dashboard_worker_resume_delete')
]
