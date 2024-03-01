import os
from requests.auth import HTTPBasicAuth
from urllib.parse import quote_plus

KEY_311 = os.environ.get('311_API_KEY')
AUTH_311 = HTTPBasicAuth('key', KEY_311)
API_URL_311 = 'https://boston2-production.spotmobile.net/open311/v2/services.json'
ILLEGAL_PARKING_SERVICE_CODE = quote_plus("Transportation - Traffic Division:Enforcement & Abandoned Vehicles:Parking Enforcement")