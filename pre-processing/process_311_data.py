import json
import pickle


def extract_request_id_with_description(filename:str) -> dict:
    ''' 
    For a given file containing a JSON Array of Service Request JSON Objects, extract the service number and the description
    (if it exists) into a dictionary for further preprocessing.

    Returns: Dict (Service Request ID -> Service Request Description)
    '''
    request_id_descr_dict = {}
    service_requests_json = json.loads(open(filename, 'r').read())

    for service_request in service_requests_json:
        # Ensure the description exists for this service request
        description = service_request.get('description', False)
        if not description: continue   

        # Add to dictionary using service request ID as key and service request description as value.
        request_id_descr_dict[service_request['service_request_id']] = service_request['description']

    return request_id_descr_dict


# Create dictionary and store it as a python pickle file for later use.    
service_requests_with_description_file = open('service_req_desc_03-02-24_01_09_24.pkl', 'wb')

dict = extract_request_id_with_description('all_service_requests.json')

pickle.dump(dict, service_requests_with_description_file)

service_requests_with_description_file.close()
