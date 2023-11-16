import json

data = {}
with open('../static/maps/argentina/data_departamentos.geojson') as f:
  data = json.load(f)

geometry = {}
with open('../static/maps/argentina/departamentos.geojson') as f:
  geometry = json.load(f)


print(geometry['features'][0]['properties'])

for geo in geometry['features']:
  geo['properties']['PROVINCIA'] = None
  for entry in data['features']:
    if geo['properties']['NAM'] == entry['properties']['nombre']:
      geo['properties']['PROVINCIA'] = entry['properties']['provincia']['nombre']
    elif entry['properties']['nombre'] == data['features'][-1]['properties']['nombre']:
      print(geo['properties']['NAM'])
  
with open('../static/maps/argentina/departamentos-updated.geojson', 'w') as f:
  json.dump(geometry, f, indent=2)