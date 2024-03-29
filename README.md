# Fetch Take-Home Exercise — Site Reliability Engineering - Solution
- I have used Python 3.10.11 to implement a program that checks the health of a set of HTTP endpoints from a given YAML file path as command line argument

## Installation and Environment Setup
1. Install Python 3.10.11 and pip 23.0.1 if you haven't already: https://www.python.org
2. Unzip the file.
3. Open a terminal or command prompt in the directory where the unzipped folder is located.
4. Create a virtual environment and activate it.
```
python -m venv venv
# Activating on Windows: venv\Scripts\activate
# Activating on Linux and macOS: source venv/bin/activate
```
5. Installed the required packages
``` 
pip install -r requirements.txt
``` 
This will include PyYAML and requests library, which we use to read YAML file and make HTTP/HTTPS requests respectively.

## Steps to execute the program -
1. Open the terminal with your virtual environment being created earlier.
2. Copy the YAML file path - Full path along with file name. Or if in same directory, then just the name will be fine.
3. Run the following command on your terminal:
```
python fetch_sre_test_endpoints.py "<FILE_PATH_TO_YAML_FILE_IN_QUOTES>"
```
5. Replace the `<FILE_PATH_TO_YAML_FILE_IN_QUOTES>` with your copied file path address.
6. Hit enter to execute the program.


**_NOTE:_** Make sure you have python added to your system environment variables, otherwise you might encounter an error when executing the script from command line.

## Output
https://fetch.com/ - Status Code:200, Latency:107.54ms --> Status = UP\
https://fetch.com/careers - Status Code:200, Latency:69.49ms --> Status = UP\
https://fetch.com/some/post/endpoint - Status Code:403, Latency:92.02ms --> Status = DOWN\
https://www.fetchrewards.com/ - Status Code:200, Latency:310.42ms --> Status = UP

Results after Test cycle #1 ends:

fetch.com has 67% availability percentage\
www.fetchrewards.com has 100% availability percentage

---

https://fetch.com/ - Status Code:200, Latency:75.20ms --> Status = UP\
https://fetch.com/careers - Status Code:200, Latency:79.91ms --> Status = UP\
https://fetch.com/some/post/endpoint - Status Code:403, Latency:67.73ms --> Status = DOWN\
https://www.fetchrewards.com/ - Status Code:200, Latency:248.95ms --> Status = UP

Results after Test cycle #2 ends:

fetch.com has 67% availability percentage\
www.fetchrewards.com has 100% availability percentage

---

Ctrl+C detected. Exiting the program.
