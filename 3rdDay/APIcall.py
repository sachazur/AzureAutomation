import requests
import json
import pprint

#get the current position of ISS
url="http://api.open-notify.org/iss-now.json"
print("getting ISS lat long")
r=requests.get(url)
print(r.text)
response=json.loads(r.text)
print (response.get('iss_positions'))
lat=response.get('iss_position').get('latitude')
long=response.get('iss_position').get('longitude')
print(lat,long)


#map that place on globe
latlng="{},{}".format(lat,long)
payload= {'latlng':latlng}

mapurl='http://maps.googleapis.com/maps/api/geocode/json'
print("getting ISs location")
r =requests.get(mapurl,params=payload)
response=json.loads(r.text)
pprint.pprint(response)
print("*"*50)
