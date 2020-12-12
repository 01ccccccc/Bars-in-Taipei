# import googlemaps
# import pprint
# import time
# # from GoogleMapsAPIKey import get_my_key

# # Define our API Key
# # API_KEY = get_my_key()
# API_KEY = 'AIzaSyBcpx_10jVDX6EJDPuEB7TUgDC33f7WSZM'

# # Define our Client
# gmaps = googlemaps.Client(key = API_KEY)

# # Define our Search
# places_result = gmaps.places_nearby(location = '-33.8670522, 151.1957362', radius = 400000, open_now = False, type = 'cafe')

# # pprint.pprint(places_result)

# # # pause the script for 3 seconds
# # time.sleep(3)

# # # get the next 20 results 
# # places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])

# # loop through each place in the results
# for place in places_result['results']:

#     # define my place id
#     my_place_id = place['place_id']

#     # define the fields we want went back to us
#     my_fileds = ['name', 'formatted_phone_number', 'type']

#     # make a requests for the details
#     place_details = gmaps.place(place_id = my_place_id, fields = my_fileds)

#     # print the results
#     print(place_details)

import requests
import json
from urllib.parse import urlencode
import time

# output = 'json'
# place_id = 'ChIJGRfASgmpQjQRD4tpHWauFLU'
# key = 'AIzaSyBcpx_10jVDX6EJDPuEB7TUgDC33f7WSZM'

# url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name,rating,formatted_phone_number&key=AIzaSyBcpx_10jVDX6EJDPuEB7TUgDC33f7WSZM'
url_base = f"https://maps.googleapis.com/maps/api/place/details/json"

parameters = {
    'key':'AIzaSyBcpx_10jVDX6EJDPuEB7TUgDC33f7WSZM',
    'place_id':'ChIJGRfASgmpQjQRD4tpHWauFLU',
    'fields':'opening_hours,place_id',
    'language':'zh-TW'
}

para_encoded = urlencode(parameters)
url = f'{url_base}?{para_encoded}'

r = requests.get(url)
results = r.json()['result']

print(results)
# opening_hour = []
# lst = [opening_hour]
# key = 'opening_hours'
# for n in range(len(results)):
#     na_input(lst, key, results[n])



