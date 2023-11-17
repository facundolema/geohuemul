import json

dep = {}
with open('./raw/departamentos.geojson') as f:
  dep = json.load(f)

provincias = {
  "Ciudad Autónoma de Buenos Aires": {
    "id": 0,
    "name": "caba"
  },
  "Buenos Aires": {
    "id": 1,
    "name": "buenos_aires"
  },
  "Catamarca": {
    "id": 2,
    "name": "catamarca"
  },
  "Chaco": {
    "id": 3,
    "name": "chaco"
  },
  "Chubut": {
    "id": 4,
    "name": "chubut"
  },
  "C\u00f3rdoba": {
    "id": 5,
    "name": "cordoba"
  },
  "Corrientes": {
    "id": 6,
    "name": "corrientes"
  },
  "Entre R\u00edos": {
    "id": 7,
    "name": "entre_rios"
  },
  "Formosa": {
    "id": 8,
    "name": "formosa"
  },
  "Jujuy": {
    "id": 9,
    "name": "jujuy"
  },
  "La Pampa": {
    "id": 10,
    "name": "la_pampa"
  },
  "La Rioja": {
    "id": 11,
    "name": "la_rioja"
  },
  "Mendoza": {
    "id": 12,
    "name": "mendoza"
  },
  "Misiones": {
    "id": 13,
    "name": "misiones"
  },
  "Neuqu\u00e9n": {
    "id": 14,
    "name": "neuquen"
  },
  "R\u00edo Negro": {
    "id": 15,
    "name": "rio_negro"
  },
  "Salta": {
    "id": 16,
    "name": "salta"
  },
  "San Juan": {
    "id": 17,
    "name": "san_juan"
  },
  "San Luis": {
    "id": 18,
    "name": "san_luis"
  },
  "Santa Cruz": {
    "id": 19,
    "name": "santa_cruz"
  },
  "Santa Fe": {
    "id": 20,
    "name": "santa_fe"
  },
  "Santiago del Estero": {
    "id": 21,
    "name": "santiago_del_estero"
  },
  "Tierra del Fuego, Antártida e Islas del Atlántico Sur": {
    "id": 22,
    "name": "tierra_del_fuego"
  },
  "Tucum\u00e1n": {
    "id": 23,
    "name": "tucuman"
  }
}

for d in dep['features']:
  d['properties']['pid'] = provincias[d['properties']['PROVINCIA']]['id']
  d['properties']['pname'] = provincias[d['properties']['PROVINCIA']]['name']

with open('deparamentos.json', 'w') as g:
  json.dump(dep, g, indent=2)
  