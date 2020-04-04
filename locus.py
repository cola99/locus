from glob import glob
from GPSPhoto import gpsphoto
import folium


# Put the script inside the same folder that contains the JPG'S.
data = glob("*.jpg")
all_coords = []

for x in data:
    data = gpsphoto.getGPSData(x)
    all_coords.append([data.get("Latitude"), data.get("Longitude")]) # Get only the lat,long keys.
    

# Build map with folium and map coordinates from the list.
m = folium.Map(location=[51.501622222222224, -0.1407861111111111], zoom_start=5) # Default location is a view of United Kingdom.
for coord in all_coords: 
    folium.Marker(location=coord).add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
m.add_child(folium.LatLngPopup())
m.save('index.html') # Write everything to a HTML document.
