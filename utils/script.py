import json, csv

countries = []
data = []
new = {
  "type": "FeatureCollection",
  "crs": {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
  "features": []
}

with open('../static/world.geojson') as f:
  countries = json.load(f)

with open('../static/data.json') as f:
  data = json.load(f)

for country in countries['features']:
  for country_data in data:
    if country_data['admin'] == country['properties']['ADMIN']:
      new['features'].append({
        "type": "Feature",
        "properties": country_data,
        "geometry": country['geometry']
      })
      
with open('../static/world.geojson', 'w') as f:
  json.dump(new, f, indent=2)