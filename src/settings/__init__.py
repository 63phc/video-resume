from os import environ
from split_settings.tools import optional, include


ENV = environ.get('DJANGO_ENV') or 'development'

BASE_SETTINGS = [
    'components/common.py',  # standard django settings
    'components/database.py',  # sqlite


    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/%s.py' % ENV,
    # Optionally override some settings:
    optional('environments/local.py'),
]

include(*BASE_SETTINGS)
