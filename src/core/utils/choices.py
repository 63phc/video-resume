from django.utils.translation import ugettext_lazy as _


class AccountTypeChoices:
    BASIC = 'BASIC'
    PRO = 'PRO'
    ENTERPRISE = 'ENTERPRISE'

    CHOICES = (
        (BASIC, _('Basic')),
        (PRO, _('Professional')),
        (ENTERPRISE, _('Enterprise'))
    )
