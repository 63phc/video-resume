from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView

from src.apps.users.views import RegistrationView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('role_choice/', TemplateView.as_view(
        template_name='registration/role_choice.html'), name='sign_up'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/register/user/', RegistrationView.as_view(),
         name='registration-user'),
    path('accounts/register/hr/', RegistrationView.as_view(),
         name='registration-hr'),
    path('accounts/register/profile/', ProfileView.as_view(), name='registration-profile'),
    path('dashboard/worker/', include('src.apps.account_worker.urls'),
         name='dashboard_worker'
    ),
    path('dashboard/hr/', TemplateView.as_view(
        template_name='dashboard_hr/dashboard_hr.html'),
         name='dashboard_hr'),
    path('accounts/', include('src.apps.users.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
