<script lang="ts">
	import Map from '$components/Map.svelte';
	import { onMount } from 'svelte';
	import * as d3 from 'd3';

	let [width, height] = [900, 900];

  let projection = d3
		.geoAzimuthalEquidistant()
    .rotate([58.38, 34.6])
		.scale(135)
		.translate([width / 2, height / 2]);

	let data: any = undefined;

	onMount(async () => {
	  const response = await fetch('/maps/world.geojson');
	  data = await response.json();
	});
</script>

<div class="h-full w-full flex justify-center items-center">
  {#if data}
	  <Map {projection} {width} {height} data={data.features} graticule/>
  {:else}
	  <p>loading...</p>
  {/if}
</div>

<style>
	p {
		color: white;
	}
</style>