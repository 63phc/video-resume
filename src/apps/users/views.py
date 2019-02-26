from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from src.core.utils.choices import AccountTypeChoices

from src.apps.account_hr.models import AccountHr
from src.apps.account_worker.models import AccountWorker

from .forms import RegistrationForm, ProfileForm

User = get_user_model()


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('registration-profile')

    def form_valid(self, form):
        new_user = form.save()
        if form.cleaned_data['account'] == 'user':
            account = AccountWorker.objects.create(
                type_account=AccountTypeChoices.BASIC,
                worker=new_user
            )
        elif form.cleaned_data['account'] == 'hr':
            account = AccountHr.objects.create(
                type_account=AccountTypeChoices.BASIC,
                id_user=new_user
            )
        account.save()
        new_user.save()
        login(self.request, new_user)
        return super().form_valid(form)


class ProfileView(FormView):
    form_class = ProfileForm

    def get_template_names(self):
        user = get_object_or_404(User, username=self.request.user)
        return [
            'registration/registration_profile.html']

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        user = get_object_or_404(User, username=self.request.user)
        if AccountHr.objects.filter(id_user=user).exists():
            dashboard_url = reverse_lazy('dashboard_hr')
        elif AccountWorker.objects.filter(worker=user).exists():
            worker = AccountWorker.objects.get(worker=user)
            dashboard_url = reverse_lazy(
                'dashboard_worker:dashboard_worker_main',
                kwargs={'pk': worker.pk}
            )
        else:
            raise Http404
        return dashboard_url
