import googlemaps

gmaps = googlemaps.Client(key='Your_API_key')
my_dist = gmaps.distancematrix('Delhi','Mumbai')['row'][0]['elements'][0]

print(my_dist)
