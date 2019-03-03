from django.urls import path


urlpatterns = [
    path('', HRDashboardView.as_view(), name='main'),
]
