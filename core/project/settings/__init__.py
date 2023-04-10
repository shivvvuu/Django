import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Name spacing our own custom environment variables
ENVVAR_SETTING_PREFIX = 'CORESETTINGS_'

LOCAL_SETTING_PATH = os.getenv(f'{ENVVAR_SETTING_PREFIX}LOCAL_SETTINGS_PATH')

if not LOCAL_SETTING_PATH:
    LOCAL_SETTING_PATH = 'local/settings.dev.py'

if not os.path.isabs(LOCAL_SETTING_PATH):
    LOCAL_SETTING_PATH = str(BASE_DIR / LOCAL_SETTING_PATH)

include('base.py', 'logging.py', 'custom.py', optional(LOCAL_SETTING_PATH), 'envvars.py', 'docker.py')
