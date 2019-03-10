from django.urls import path

from .views import HRDashboardView, AccountHrCreateView

app_name = 'account_hr'
urlpatterns = [
    path('<pk>/', HRDashboardView.as_view(), name='main'),

]
