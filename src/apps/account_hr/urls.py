from django.urls import path

from .views import HRDashboardView

app_name = 'account_hr'
urlpatterns = [
    path('<pk>/', HRDashboardView.as_view(), name='dashboard_hr_main'),
]
