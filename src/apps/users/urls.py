from django.urls import path
from django.conf.urls import include

from src.apps.users.views import RegistrationView, ProfileView, LoginView


urlpatterns = [
    path('register/worker/', RegistrationView.as_view(),
         name='registration-user'),
    path('register/hr/', RegistrationView.as_view(),
         name='registration-hr'),
    path('register/profile/', ProfileView.as_view(),
         name='registration-profile'),
    path('login/', LoginView.as_view(),
         name='login'),
    path('', include('django.contrib.auth.urls')),
]
