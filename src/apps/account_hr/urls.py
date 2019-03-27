from django.urls import path

from .views import DashboardView, AccountHrCreateView


app_name = 'account_hr'

urlpatterns = [
    path('<pk>/', DashboardView.as_view(), name='main'),

]
