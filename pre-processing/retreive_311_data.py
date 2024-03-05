import requests
import constants
import json
import time

def execute_single_query(page_num:int):
    ''' 
    Sends an HTTP GET request to the Boston 311 API for Illegal Parking.
    Requests 100 (maximum allowed) service requests for a given page.
    
    Returns: HTTP Response Object
    '''
    query_url = f'https://boston2-production.spotmobile.net/open311/v2/requests.json?service_code={constants.ILLEGAL_PARKING_SERVICE_CODE}&per_page=100&page={page_num}'

    return requests.get(url=query_url, auth=constants.AUTH_311)

def retreive_all_service_requests(filename:str):
    ''' 
    Continually sends HTTP Requests to the Boston 311 API for Illegal Parking Service Requests.
    Concatenates responses into a single JSON Array containing Service Request JSON Objects.
    Updates are sent to the console throughout the process.
    Returns: writes the JSON Array to the given filename, once all service requests are received.
    '''

    # Executes first query
    page = 1
    current_response = execute_single_query(page)

    # Ensure HTTP Error is captured
    if current_response.status_code != 200:
        print(f'First Query failed. Error code: {current_response.status_code}')
        return
    page+=1
    
    # Creates JSON Array Object on response
    all_service_requests_json = current_response.json()

    # Continually execute queries for the next page until there are no more (Error Code != 200, 429)
    while True:
        current_response = execute_single_query(page)
        status_code = current_response.status_code

        # Successful response has service request JSON Objects concatenated to end of overall JSON Array
        if status_code == 200:
            print(f'Query Received: {page}')
            for service_request_obj in current_response.json():
                all_service_requests_json.append(service_request_obj)
            page += 1
        
        # Error code 429 indicates rate limiting (10 GET Requests per min)
        elif status_code == 429:
            print(f'Rate Limited: Waiting 1 minute. \n Current Page {page}')
            # Wait 60 seconds to resume query
            time.sleep(60)
            print('Resuming Query...')
        
        # Any other error code, break loop.
        else: 
            print(f'Error recieved: {status_code}')
            break

    print(f'Finished querying. Total pages queried: {page}\n Printing...')

    # Write received service requests to specificed filename
    all_service_requests_file = open(filename, 'w')
    all_service_requests_file.write(json.dumps(all_service_requests_json))
    all_service_requests_file.close()

retreive_all_service_requests()