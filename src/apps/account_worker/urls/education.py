from django.urls import path

from ..views import (
    EducationUpdateView, EducationCreateView,
    EducationDeleteView
)


app_name = 'dashboard_worker'

urlpatterns = [
    path(
        'education/update/<pk>/<resume_pk>/<worker_pk>',
        EducationUpdateView.as_view(),
        name='dashboard_worker_education_update'
    ),
    path('education/create/<resume_pk>/<worker_pk>',
         EducationCreateView.as_view(),
         name='dashboard_worker_education_create'),
    path(
        'education/delete/<pk>/<resume_pk>/<worker_pk>',
        EducationDeleteView.as_view(),
        name='dashboard_worker_education_delete'
    )
]
