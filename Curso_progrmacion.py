import googlemaps
from datetime import datetime

# Ingresar la clave de la API de Google Maps
gmaps = googlemaps.Client(key='A12345HDF')

# Ingresar los puntos de inicio y destino
origen = 'Ciudad de Mexico'
destino = 'Guadalajara'

# Obtener la información de la ruta
now = datetime.now()
directions_result = gmaps.directions(origen, destino, mode="driving", departure_time=now)

# Seleccionar la mejor ruta
best_route = None
best_duration = float('inf')
for route in directions_result:
    duration = route['legs'][0]['duration']['value']
    if duration < best_duration:
        best_duration = duration
        best_route = route

# Mostrar la mejor ruta al usuario
print('La mejor ruta es:')
for step in best_route['legs'][0]['steps']:
    print(step['html_instructions'])