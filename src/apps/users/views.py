from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.views import LoginView as LoginViewMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from src.core.utils.choices import AccountTypeChoices

from src.apps.account_hr.models import AccountHr
from src.apps.account_worker.models import AccountWorker

from .forms import RegistrationForm, ProfileForm, LoginForm


User = get_user_model()


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('registration-profile')

    def form_valid(self, form):
        new_user = form.save()
        ACCOUNT_MAP = {
            'user': AccountWorker,
            'hr': AccountHr,
        }
        account_model = ACCOUNT_MAP.get(form.cleaned_data['account'])
        if not account_model:
            raise Http404
        account_model.objects.create(
            type_account=AccountTypeChoices.BASIC,
            user=new_user)
        login(self.request, new_user)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileView(FormView):
    form_class = ProfileForm
    template_name = 'registration/registration_profile.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        user = get_object_or_404(User, username=self.request.user)
        worker = user.workers_related.all().first()
        hr = user.hrs_related.all().first()
        if hr:
            return hr.get_absolute_url()
        else:
            return worker.get_absolute_url()


class LoginView(LoginViewMixin):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        user = get_object_or_404(User, username=self.request.user)
        worker = user.workers_related.all().first()
        hr = user.hrs_related.all().first()
        if worker:

            return worker.get_absolute_url()
        else:
            return hr.get_absolute_url()
