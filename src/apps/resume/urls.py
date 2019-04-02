from django.urls import path

from .views import ResumeDetailView

app_name = 'resume'

urlpatterns = [
    path('detail/<int:pk>/',
         ResumeDetailView.as_view(), name='detail'),
]
