import os
from base64 import b64encode

SECRET_KEY = b64encode(os.urandom(64)).decode('utf-8')[:30]
WTF_CSRF_KEY = b64encode(os.urandom(64)).decode('utf-8')[:30]
WTF_CSRF_SECRET_KEY = b64encode(os.urandom(64)).decode('utf-8')[:30]

# Database settings
MONGODB_SETTINGS = {
    'db': 'wevesidb',
    'host': 'vm.local'
}

# Login Settings
LOGIN_VIEW = "login"

# Debug Toolbar
DEBUG_TB_PROFILER_ENABLED = True

