<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';
  import { downloadImage } from '$lib/functions';

	function drawMap() {
		let container = d3.select('#map-container');
		let [width, height] = [1280, 960];
		
		let projection = d3.geoAlbers()
    .rotate([-20.0, 0.0])
    .center([0.0, 52.0])
    .parallels([35.0, 65.0])
    .translate([width / 2, height / 2])
    .scale(1200)
    .precision(.1)
		
		let path = d3.geoPath().projection(projection);

		let svg = container
			.append('svg')
			.attr('width', width)
			.attr('height', height)
      .attr('xlmns', 'http://www.w3.org/2000/svg')
      .attr('xmlns:xlink', "http://www.w3.org/1999/xlink")

		let g = svg.append('g').attr('class', 'map');
    
		d3.json('/world.geojson').then(function (data) {
      g.selectAll('path')
      .data(data.features)
      .enter()
      .append('path')
      .attr('d', path)
      .style('fill', "#8093F1")
      .style('stroke', "#fff")
      .style('stroke-width', 1)
      
		});
  }

	onMount(drawMap);

</script>

<div id="map-container">
	
</div>
<button on:click={downloadImage}>Download</button>

<style>
	#map-container {
		height: 100%;
	}
</style>
