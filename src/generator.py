import geopandas
import folium
import pandas
import geopy
import os

dataframe = pandas.read_csv("data.csv")

names = list(dataframe["name"])
addresses = list(dataframe["address"])
websites = list(dataframe["website"])

title = "Sacramento Arts Map"
subtitle = ""
mainlink = ""

locator = geopy.geocoders.Nominatim(user_agent='myGeocoder')

# split = addresses[0].split(', ')
# # print(split)

# lastele = split[len(split) - 1]
# address = list(locator.geocode(lastele))
# city = address[0].split(', ')[1]
location = locator.geocode("Sacramento, CA")

# loclist = [location.latitude - 0.0225, location.longitude]
loclist = [38.568930, -121.477000]

try:
   map = folium.Map(location=loclist, zoom_start=13.4, tiles="Stamen Toner")
except:
   map = folium.Map(location=loclist, zoom_start=13.4)

for name, address, website in zip(names, addresses, websites):
  location = locator.geocode(address)
  print(f"\n{name}\n")
  print(f"\n{address}\n")
  print(f"\n{website}\n")
  loclist = [location.latitude, location.longitude]
  map.add_child(folium.Marker(
      location=loclist,
      popup=f"<div style='width: 300px;'><h4>{name}</h4>\n{address}<br><a target='new' href='{website}'>{website}</a></div>",
      icon=folium.Icon(color='black', icon='')
  )
  )

map.save("index.html")

f = open("index.html", "r")
contents = f.readlines()
f.close()

contents.insert(34, "".join('<link rel="stylesheet" href="generator_2.css"/>'))
contents.append('<script src="generator_2.js"></script>')

f = open("index.html", "w")
contents = "".join(contents)
f.write(contents)
f.close()
