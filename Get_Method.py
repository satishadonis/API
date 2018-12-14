# Get all security questions

import requests
import json
from pprint import pprint


url = "http://10.10.220.99:92/api/v1/Account/SecurityQuestions"

response = requests.get(url)
resp =response.json()

# print(resp)
# Debug internally
# import ipdb; ipdb.set_trace()


# Validations

if response.status_code == 200:
    print(response.status_code,"-->", response.reason,'\n',pprint(response.json(),indent=4),"Success")
else:
    print(response.status_code,"-->", response.reason,'\n',pprint(response.json(),indent=4), "Failed")

# Parsing
security_questions = [d['Text'] for d in resp]
print(security_questions)


