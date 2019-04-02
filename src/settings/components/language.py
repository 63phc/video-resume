from django.utils.translation import ugettext_lazy as _
from src.settings.components.common import project_dir


LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    project_dir + "/apps/locale",
)
