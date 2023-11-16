<svelte:head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
</svelte:head>

<script>
  import { onMount } from 'svelte';
  import { color } from '$lib/constants'
  import Input from '$components/Input.svelte';
  let L;

  onMount(async () => {
    L = (await import('leaflet')).default;
    const map = L.map('map', {
      center: [-37.3, -60],
      zoom: 6.9,
      zoomSnap: 0.1,
    });

    const response = await fetch('/maps/argentina/departamentos.json');
    let geojson = await response.json();
    L.geoJSON(geojson,
      {
        onEachFeature: (feature, layer) => {
          // layer.bindPopup(feature.properties.NAM);
          layer.on('click', () => {
            layer.setStyle({
              color: '#000',
              fillColor: color.red,
              weight: 1.5,
              fillOpacity: 1,
            });
          })
          layer.on('add', () => {
            layer._path.setAttribute('data', feature.properties.NAM.toLowerCase())
            }
          )
        },
        style: (feature) => {
          return {
            color: '#000',
            fillColor: color.beige,
            weight: 1.5,
            fillOpacity: 1,
          }
        }
      }
    )
      .addTo(map);
  });
</script>

<style>
  #map {
    height: 900px;
    width: 900px;
    border: 1px solid black;
  }

  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: white;
    width: 100%;
    height: 100%;
  }
</style>

<div class="container">
  <div id="map"/>
  <Input 
    onkeyup={(e) => {
      if (e.key === 'Enter') {
        const input = e.target;
        const value = input.value.toLowerCase();
        const layer = document.querySelector(`[data="${value}"]`);
        if (layer) {
          console.log(layer)
          layer.style.fill = color.red;
          console.log(layer)
          input.value = '';
        }
      }
    }}
  />
</div>
