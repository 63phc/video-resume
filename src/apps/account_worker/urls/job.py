from django.urls import path

from ..views import JobCreateView, JobUpdateView, JobDeleteView


app_name = 'dashboard_worker'

urlpatterns = [
    path('job/create/<resume_pk>/<w_pk>', JobCreateView.as_view(),
         name='dashboard_worker_job_create'),
    path('job/update/<pk>/<resume_pk>/<w_pk>', JobUpdateView.as_view(),
         name='dashboard_worker_job_update'),
    path('job/delete/<pk>/<resume_pk>/<w_pk>', JobDeleteView.as_view(),
         name='dashboard_worker_job_delete'),
]
