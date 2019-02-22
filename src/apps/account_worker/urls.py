from django.urls import path
from .views import (
    AccountWorkerView,
    ResumeListView,
    ResumeUpdateView,
    ResumeCreateView,
    ResumeDeleteView,
    EducationUpdateView,
    EducationCreateView,
    EducationDeleteView,
    SkillCreateView,
    SkillUpdateView,
    SkillDeleteView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView
)


app_name = 'dashboard_worker'

urlpatterns = [
    path('<pk>', AccountWorkerView.as_view(), name='dashboard_worker_main'),
    # Resume
    path(
        'resume/<pk>',
        ResumeListView.as_view(),
        name='dashboard_worker_resume'
    ),
    path(
        'resume/create/<w_pk>',
        ResumeCreateView.as_view(),
        name='dashboard_worker_resume_create'
    ),
    path('resume/update/<pk>/<w_pk>', ResumeUpdateView.as_view(),
         name='dashboard_worker_resume_update'),
    path('resume/delete/<pk>/<w_pk>', ResumeDeleteView.as_view(),
         name='dashboard_worker_resume_delete'),
    # Education
    path(
        'education/update/<pk>/<res_pk>/<w_pk>',
        EducationUpdateView.as_view(),
        name='dashboard_worker_education_update'
    ),
    path('education/create/<res_pk>/<w_pk>', EducationCreateView.as_view(),
         name='dashboard_worker_education_create'),
    path(
        'education/delete/<pk>/<res_pk>/<w_pk>',
        EducationDeleteView.as_view(),
        name='dashboard_worker_education_delete'
    ),
    # Skill
    path('skill/create/<res_pk>/<w_pk>', SkillCreateView.as_view(),
         name='dashboard_worker_skill_create'),
    path('skill/update/<pk>/<res_pk>/<w_pk>', SkillUpdateView.as_view(),
         name='dashboard_worker_skill_update'),
    path('skill/delete/<pk>/<res_pk>/<w_pk>', SkillDeleteView.as_view(),
         name='dashboard_worker_skill_delete'),
    # Job
    path('job/create/<res_pk>/<w_pk>', JobCreateView.as_view(),
         name='dashboard_worker_job_create'),
    path('job/update/<pk>/<res_pk>/<w_pk>', JobUpdateView.as_view(),
         name='dashboard_worker_job_update'),
    path('job/delete/<pk>/<res_pk>/<w_pk>', JobDeleteView.as_view(),
         name='dashboard_worker_job_delete'),
]
