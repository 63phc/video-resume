from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

from src.apps.users.views import RegistrationView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('accounts/register/user/', RegistrationView.as_view(),
         name='registration-user'),
    path('accounts/register/hr/', RegistrationView.as_view(),
         name='registration-hr'),
    path('accounts/register/profile/', ProfileView.as_view(),
         name='registration-profile'),
    path('dashboard/worker/', TemplateView.as_view(
        template_name='dashboard_worker/dashboard_worker.html'
    ),
         name='dashboard_worker'
    ),
    path('dashboard/hr/', TemplateView.as_view(
        template_name='dashboard_hr/dashboard_hr.html'
    ),
         name='dashboard_hr'
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('vacancies/', include('src.apps.vacancy.urls'), name='vacancies'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
