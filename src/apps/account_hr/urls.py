from django.urls import path

from .views import HRDashboardView

urlpatterns = [
    path('', HRDashboardView.as_view(), name='main'),
]
