from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class UserCheckingFirstQueryset(models.QuerySet):
    def is_exist(self, **kwargs):
        value = kwargs.get('username')
        return self.filter(username=value).first()


class User(AbstractBaseUser, PermissionsMixin):
    """ Class model custom User """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    profile = models.ForeignKey(
        'Profile', on_delete=models.CASCADE, null=True, blank=True
    )  # null=True, blank=True for createsuperuser

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()
    checking = UserCheckingFirstQueryset.as_manager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class Profile(models.Model):
    """ class user data (foreignkey model User) """

    FAMILY_STATUS_CHOICES = (
        ('1', _('single')),
        ('2', _('married')),
        ('3', _('widowed')),
        ('4', _('divorced'))
    )

    first_name = models.CharField(_('first name'), max_length=20)
    second_name = models.CharField(_('second name'), max_length=20)
    birth = models.DateField(_('birth date'))
    city = models.CharField(_('city'), max_length=20)
    family_status = models.CharField(
        _('family status'), max_length=20, choices=FAMILY_STATUS_CHOICES
    )
    phone = models.CharField(_('phone number'), unique=True, max_length=15)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return self.first_name
