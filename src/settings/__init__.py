from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # standard django settings
    'components/language.py',  # language settings

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/%s.py' % ENV,
]

# Include settings:
include(*base_settings)
