import os
from requests.auth import HTTPBasicAuth

KEY_311 = os.environ.get('311_KEY')
AUTH_311 = HTTPBasicAuth('key', KEY_311)
API_URL_311 = 'https://boston2-production.spotmobile.net/open311/v2/services.json'