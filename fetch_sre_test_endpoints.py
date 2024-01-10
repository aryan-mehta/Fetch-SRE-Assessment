'''
file_name:      fetch_sre_test_endpoints.py
description:    This script is used to test the endpoints of SRE's RESTful API server. 
                It uses PyYAML to read YAML file and requests library to test the endpoints.
input:          File path as command line argument 
                >>python fetch_sre_test_endpoints.py "<FILE_PATH_TO_YAML_FILE_IN_QUOTES>"
output:         Availability percentage of each URL domain over the lifetime of the program.
author:         Aryan Mehta <amehta64@asu.edu>
'''
import time
import sys
import yaml
import requests

def read_yaml(file_path):
    """
    Read a YAML file and return the loaded data.

    Parameters:
    - file_path (str): The path to the YAML file to be read.

    Returns:
    - dict or list: The loaded YAML data as a dictionary or a list,
                    depending on the structure of the YAML file.

    Raises:
    - FileNotFoundError: If the specified file_path does not exist.
    - yaml.YAMLError: If there is an error in parsing the YAML file.
    - Exception: Any other exception encountered during the process.

    Example:
    >>> data = read_yaml('configuration.yaml')
    >>> print(data)
    {'key': 'value'}
    """
    try:
        # Read YAML file
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        # Return the loaded yaml data
        return data
    except Exception as e:
        print(e)
        sys.exit(0)

def test_endpoint(url, method, headers, body):
    """
    Test the availability of an endpoint by making an HTTP request.

    Parameters:
    - url (str): The URL of the endpoint to be tested.
    - method (str): The HTTP method to use for the request (e.g., 'GET', 'POST').
    - headers (dict): A dictionary of HTTP headers to include in the request.
    - body (str or dict): The request body, either as a string or a dictionary for 'POST' requests.

    Returns:
    - str: 'UP' if the endpoint is reachable and meets criteria, 'DOWN' otherwise.

    Raises:
    - requests.RequestException: If there is an issue with the HTTP request.

    Example:
    >>> url = 'https://example.com/api/endpoint'
    >>> method = 'GET'
    >>> headers = {'User-Agent': 'MyApp/1.0'}
    >>> body = None
    >>> result = test_endpoint(url, method, headers, body)
    >>> print(result)
    'UP'
    """
    try:
        start_time = time.time()
        response = requests.request(method=method, url=url, headers=headers, data=body, timeout=5)
        latency = (time.time() - start_time) * 1000  # Convert to milliseconds

        if response.status_code // 100 == 2 and latency < 500:
            print(f'{url} - Status Code:{response.status_code}, Latency:{latency:.2f}ms', end="")
            print(' --> Status = UP')
            return 'UP'
        print(f'{url} - Status Code:{response.status_code}, Latency:{latency:.2f}ms', end="")
        print(' --> Status = DOWN')
        return 'DOWN'
    except requests.RequestException:
        print(f'{url} - Status = DOWN')
        return 'DOWN'

def run_tests(yaml_data):
    """
    Continuously test a list of endpoints and log availability percentages.

    This function runs an infinite loop, testing the availability of each endpoint
    specified in a YAML file. It logs the availability percentage for each domain
    to the console after each test cycle.

    The script can be interrupted by the user (Ctrl+C) to gracefully exit the program.

    YAML Data Structure:
    - Each YAML data entry should represent an endpoint with the following structure:
    {'url': 'endpoint_url', 'method': 'GET', 'headers': {'key': 'value'}, 'body': 'request_body'}

    Returns:
    - None
    - Prints the availability percentage of each URL domain over the lifetime of the program.

    Raises:
    - KeyboardInterrupt: If the user interrupts the program with Ctrl+C.

    Example:
    >>> run_tests(yaml_data)
    Results after Test cycle #1 ends:
    fetch.com has 33% availability percentage
    fetchrewards.com has 100% availability percentage
    ---------------------------------------------------------------------------

    Results after Test cycle #2 ends:
    fetch.com has 67% availability percentage
    fetchrewards.com has 50% availability percentage
    ---------------------------------------------------------------------------
    """
    cycle_count = 0
    try:
        while True:
            cycle_count += 1
            # Results dictionary will contain information about domain: status
            results = {}

            # Test each endpoint from YAML file
            for data in yaml_data:
                url = data.get('url')
                method = data.get('method','GET')
                headers = data.get('headers')
                body = data.get('body')
                status = test_endpoint(url, method, headers, body)
                domain = url.split('/')[2]
                if domain in results:
                    results[domain].append(status)
                else:
                    results[domain] = [status]

            # Calculate Percentage Availability and Print Output to Console
            print(f"\nResults after Test cycle #{cycle_count} ends:\n")
            for domain in results:
                domain_percentage = round((results[domain].count('UP') / len(results[domain]))*100)
                print(f"{domain} has {domain_percentage}% availability percentage")
            print("-"*75)

            # Sleep for 15 seconds
            time.sleep(15)

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting the program.")
        sys.exit(0)

# Main Function - Program Starts Here
if __name__=="__main__":
    # Specify the path to your YAML file as argument in command line
    if len(sys.argv) != 2:
        print("Usage: python fetch_sre_test_endpoints.py \"<input_file_path>\"")
        sys.exit(1)
    yaml_file_path = sys.argv[1]
    yaml_data_content = read_yaml(yaml_file_path)
    run_tests(yaml_data_content)
