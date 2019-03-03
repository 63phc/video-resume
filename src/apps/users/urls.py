from django.urls import path
from django.conf.urls import include

from src.apps.users.views import RegistrationView, ProfileView


urlpatterns = [
    path('register/user/', RegistrationView.as_view(),
         name='registration-user'),
    path('register/hr/', RegistrationView.as_view(),
         name='registration-hr'),
    path('register/profile/', ProfileView.as_view(),
         name='registration-profile'
         ),
    path('', include('django.contrib.auth.urls')),
]