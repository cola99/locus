from glob import glob
from GPSPhoto import gpsphoto
import folium
import webbrowser

# Variables list
data = glob("*.jpg") # Search the folder that contains this script for JPG's
all_coords = [] # Put all coordinates in a list format.
url = 'index.html'

for x in data:
    data = gpsphoto.getGPSData(x)
    all_coords.append([data.get("Latitude"), data.get("Longitude")]) # Get only the lat,long keys.

# Build map with folium and map coordinates from the list.
m = folium.Map(location=[51.501622222222224, -0.1407861111111111], zoom_start=5) # Default location is a view of United Kingdom.
for coord in all_coords: 
	folium.Marker(location=coord, icon=folium.Icon(color='red')).add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
m.add_child(folium.LatLngPopup())
m.save('index.html') # Write everything to a HTML document.

# Opens the HTML document in a browser.
webbrowser.open(url)

