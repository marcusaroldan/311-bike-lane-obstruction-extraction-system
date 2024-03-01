import os
from enum import Enum
from requests.auth import HTTPBasicAuth

KEY_311 = os.environ.get('311_KEY')
AUTH_311 = HTTPBasicAuth('key', KEY_311)