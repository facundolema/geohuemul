import json

countries = {}
with open('../static/world.geojson') as f:
  countries = json.load(f)


data = []
with open('../static/world-data-new.json') as f:
  data = json.load(f)


new = {
  "type": "FeatureCollection",
  "crs": {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
  "features": []
}

for country in countries['features']:
  for country_data in data:
    if country_data['adm0_a3'] == country['properties']['adm0_a3']:
      new['features'].append({
        "type": "Feature",
        "properties": country_data,
        "geometry": country['geometry']
      })
      break
    elif country_data['geounit'] == data[-1]['geounit']:
      print(country['properties']['name'])
      
with open('../static/maps/world.geojson', 'w') as f:
  json.dump(new, f, indent=2)