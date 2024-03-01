import requests
import constants 
import json
from urllib.parse import quote_plus

auth = constants.AUTH_311

def query_services():
    services_response = requests.get(url=constants.API_URL_311, auth=auth).json()

    services_file = open('services.json', 'w')
    services_file.write(json.dumps(services_response))
    services_file.close()

def query_illegal_parking():
    illegal_parking = quote_plus("Transportation - Traffic Division:Enforcement & Abandoned Vehicles:Parking Enforcement")
    query_url = f'https://boston2-production.spotmobile.net/open311/v2/requests.json?service_code={illegal_parking}&per_page=100'
    print(query_url)
    illegal_parking_response = requests.get(url=query_url, auth=auth).json()

    illegal_parking_file = open('illegal_parking_test1.json', 'w')
    illegal_parking_file.write(json.dumps(illegal_parking_response))
    illegal_parking_file.close()

query_illegal_parking()
