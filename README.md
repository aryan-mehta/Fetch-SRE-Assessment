# Fetch Take-Home Exercise — Site Reliability Engineering - Solution
- I have used Python 3.10.11 to implement a program that checks the health of a set of HTTP endpoints from a given YAML file path as command line argument

## Instructions to run the code - Environment Setup
1. Install Python 3.10.11 and pip 23.0.1 if you haven't already: https://www.python.org
2. Unzip the file
3. Open a terminal or command prompt in the directory where the unzipped folder is located.
4. Create a virtual environment using `python -m venv venv` and activate it on Windows using: `venv\Scripts\activate` or on Linux and macOS using `source venv/bin/activate`.
5. Run `pip install -r requirements.txt` to install any necessary packages (if not installed). This will include PyYAML and requests library, which we use to read YAML file and make HTTP/HTTPS requests respectively.

## Steps to execute the program -
1. Open the terminal with your virtual environment being created earlier.
2. Copy the YAML file path - Full path along with file name. Or if in same directory, then just the name will be fine.
3. Run the following command on your terminal: `python fetch_sre_test_endpoints.py "<FILE_PATH_TO_YAML_FILE_IN_QUOTES>"`
4. Replace the `<FILE_PATH_TO_YAML_FILE_IN_QUOTES>` with your copied file path address.
5. Hit enter to execute the program.


**_NOTE:_** Make sure you have python added to your system environment variables, otherwise you might encounter an error when executing the script from command line.

## Output
https://fetch.com/ - Status Code:200, Latency:107.54ms --> Status = UP\
https://fetch.com/careers - Status Code:200, Latency:69.49ms --> Status = UP\
https://fetch.com/some/post/endpoint - Status Code:403, Latency:92.02ms --> Status = DOWN\
https://www.fetchrewards.com/ - Status Code:200, Latency:310.42ms --> Status = UP\

Results after Test cycle #1 ends:\

fetch.com has 67% availability percentage\
www.fetchrewards.com has 100% availability percentage\

---

https://fetch.com/ - Status Code:200, Latency:75.20ms --> Status = UP\
https://fetch.com/careers - Status Code:200, Latency:79.91ms --> Status = UP\
https://fetch.com/some/post/endpoint - Status Code:403, Latency:67.73ms --> Status = DOWN\
https://www.fetchrewards.com/ - Status Code:200, Latency:248.95ms --> Status = UP\

Results after Test cycle #2 ends:\

fetch.com has 67% availability percentage\
www.fetchrewards.com has 100% availability percentage\

---

Ctrl+C detected. Exiting the program.


## Thank you for the Opportunity
I wanted to express my sincere gratitude for the opportunity to write the script for testing FETCH endpoints. It was truly an enjoyable experience, and I appreciate the trust and confidence you placed in me for this task.

Working on this script allowed me to apply my skills and creativity to create a robust and efficient solution. I enjoyed the challenge of ensuring the script accurately tests the endpoints while maintaining readability and flexibility.

If there are any additional improvements or modifications you'd like to discuss, please feel free to let me know. I am more than happy to refine the script further based on your feedback.

Once again, thank you for the opportunity. I look forward to collaborating on future projects and tasks.

Best regards,

Aryan Mehta