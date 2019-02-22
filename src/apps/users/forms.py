from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Select, TextInput, SelectDateWidget
from django.core.validators import EmailValidator
from src.apps.users.models import Profile

User = get_user_model()


class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[EmailValidator]
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    account = forms.CharField(
        label="hidden_field",
        widget=forms.HiddenInput(
            attrs={'id': 'account_type'}), required=False
        )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'account'
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'second_name',
            'birth',
            'city',
            'family_status',
            'phone'
        )
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'second_name': TextInput(attrs={'class': 'form-control'}),
            'birth': SelectDateWidget(
                years=range(1950, 2031),
                attrs={'class': 'form-control'},
            ),
            'city': TextInput(attrs={'class': 'form-control'}),
            'family_status': Select(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
        }
