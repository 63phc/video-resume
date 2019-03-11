from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.forms import AuthenticationForm

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

    agreeded_confidentiality = forms.BooleanField(initial=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1',
            'password2', 'account'
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'first_name', 'second_name', 'birth',
            'city', 'family_status', 'phone'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth': forms.SelectDateWidget(
                years=range(1940, 2100),
                attrs={'class': 'form-control'},
            ),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'family_status': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
