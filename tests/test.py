import requests,pprint

response = requests.get('http://localhost/phc/phcshow?action=list_customer')

pprint.pprint(response.json())