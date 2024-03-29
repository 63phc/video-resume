from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView

from src.apps.users.views import RegistrationView, ProfileView, \
    ProfileUpdateView
from src.apps.vacancy.views import tag_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('role_choice/', TemplateView.as_view(
        template_name='registration/role_choice.html'), name='sign_up'),
    path('features/', TemplateView.as_view(
        template_name='components/features.html'), name='features'),
    path('contacts/', TemplateView.as_view(
        template_name='components/contacts.html'), name='contacts'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dashboard/worker/',
         include('src.apps.account_worker.urls'),
         name='dashboard_worker'),
    path('dashboard/hr/', include('src.apps.account_hr.urls',
         namespace='dashboard_hr')),
    path('accounts/', include('src.apps.users.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('vacancies/',
         include('src.apps.vacancy.urls', namespace='vacancies')),
    path('answers/',
         include('src.apps.answer.urls', namespace='answers')),
    path('resumes/',
         include('src.apps.resume.urls', namespace='resumes')),
    path('add/tags/', tag_create_view, name='tag_create'),
    path('terms/', TemplateView.as_view(
        template_name='components/terms_of_use.html'), name='terms'),
    path('privacy/', TemplateView.as_view(
        template_name='components/privacy_policy.html'), name='privacy'),
    path('questions/',
         include('src.apps.question.urls', namespace='questions')),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
