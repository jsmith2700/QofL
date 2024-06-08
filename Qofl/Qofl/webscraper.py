import re
import requests

# Making a GET request
request = requests.get('https://www.apmex.com/search?&q=Gold%20Available%20Products&sort=price%20asc&rows=80&view=grid&version=V2&start=0')

# check status code for response received
# success code - 200
# print(r)
request_success = request
print(request_success)



# print content of request
# print(r.content)
