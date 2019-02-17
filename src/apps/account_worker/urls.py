from django.urls import path
from .views import AccountWorkerView, ResumeListView, ResumeUpdateView


app_name = 'dashboard_worker'

urlpatterns = [
    path('<pk>', AccountWorkerView.as_view(), name='dashboard_worker_main'),
    path('resume/<pk>', ResumeListView.as_view(), name='dashboard_worker_resume'),
    path('resume/update/<pk>', ResumeUpdateView.as_view(), name='dashboard_worker_resume_update'),

]
