from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

from src.apps.account_hr.views import AccountHrCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dashboard/worker/',
         include('src.apps.account_worker.urls'),
         name='dashboard_worker'),
    path('role_choice/', TemplateView.as_view(
        template_name='registration/role_choice.html'), name='sign_in'),
    path('dashboard/hr/', include('src.apps.account_hr.urls',
         namespace='dashboard_hr')),
    path('accounts/', include('src.apps.users.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('vacancies/',
         include('src.apps.vacancy.urls', namespace='vacancies')),
    path('create_account/', AccountHrCreateView.as_view(), name='create_account'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
