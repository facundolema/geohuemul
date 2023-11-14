<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';
  import { downloadImage } from '$lib/functions';

	function drawMap() {
		let container = d3.select('#map-container');
		let [width, height] = [800, 600];
		
		let projection = d3.geoMercator()
      .translate([width / 2, height / 2])
      .scale(390)
      .center([22, 5])
		
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
      .data(data.features.filter((d: any) => ["Asia", "Europe", "Africa"].includes(d.properties.continent)))
      .enter()
      .append('path')
      .attr('d', path)
      .style('fill', () => Math.random() > 0.5 ? "#70AFDB" : "#8E82C9")
      .style('stroke', "#000")
      .style('stroke-width', 1)
		});
  }

	onMount(drawMap);

</script>

<div id="map-container" />

<style>
	#map-container {
		height: 600px;
    width: 800px;
    border: 1px solid #fff
	}
</style>
