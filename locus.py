from GPSPhoto import gpsphoto
import glob
import os
import gmplot

parent_dir = (r"imgs") # Specify folder

for folder in glob.glob(os.path.join(parent_dir, '*.jpg')):
    data = gpsphoto.getGPSData(folder)
    print("Coordinates: {}\n".format(data),"Source: {}\n".format(folder))
