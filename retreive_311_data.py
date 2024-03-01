import requests
import constants
import json
import time

def execute_single_query(page_num:int):
    query_url = f'https://boston2-production.spotmobile.net/open311/v2/requests.json?service_code={constants.ILLEGAL_PARKING_SERVICE_CODE}&per_page=100&page={page_num}'

    return requests.get(url=query_url, auth=constants.AUTH_311)

def retreive_all_service_requests():
    page = 1
    current_response = execute_single_query(page)
    if current_response.status_code != 200:
        print(f'First Query failed. Error code: {current_response.status_code}')
    
    all_service_requests_json = current_response.json()

    while True:
        page += 1
        current_response = execute_single_query(page)
        status_code = current_response.status_code
        if status_code == 200:
            print(f'Query Received: {page}')
            all_service_requests_json.append(current_response.json())
        elif status_code == 429:
            print(f'Rate Limited: Waiting 1 minute. \n Current Page {page}')
            time.sleep(60)
            print('Resuming Query...')
        else: break

    print(f'Finished querying. Total pages queried: {page}\n Printing...')

    all_service_requests_file = open('all_service_requests.json', 'w')
    all_service_requests_file.write(json.dumps(all_service_requests_json))
    all_service_requests_file.close()

retreive_all_service_requests()