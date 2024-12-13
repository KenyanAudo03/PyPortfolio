import requests
 
url = 'https://api.aerisapi.com/places/closest?p=43.567,-100.895&limit=5&client_id={client_id}&client_secret={client_secret}'
response = requests.get(url)
 
if response.status_code == 200:
    data = response.json()
    if data['success']:
        ob = data['response']['ob']
        print("The current weather in Seattle is %s with a temperature of %d" % (ob['weather'].lower(), ob['tempF']))
    else:
        print("An error occurred: %s" % (data['error']['description']))
else:
    print("An error occurred while fetching data: HTTP status code %d" % response.status_code)