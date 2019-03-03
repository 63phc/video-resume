from django.urls import path

from ..views import SkillCreateView, SkillUpdateView, SkillDeleteView


app_name = 'dashboard_worker'

urlpatterns = [
    path('skill/create/<resume_pk>/<worker_pk>', SkillCreateView.as_view(),
         name='dashboard_worker_skill_create'),
    path('skill/update/<pk>/<resume_pk>/<worker_pk>',
         SkillUpdateView.as_view(),
         name='dashboard_worker_skill_update'),
    path('skill/delete/<pk>/<resume_pk>/<worker_pk>',
         SkillDeleteView.as_view(),
         name='dashboard_worker_skill_delete'),
]
