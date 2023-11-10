<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';
  import { downloadImage } from '$lib/functions';

	function drawMap() {
		let container = d3.select('#map-container');
		let [width, height] = [container.node().clientWidth, container.node().clientHeight];
		
		let projection = d3
			.geoAzimuthalEqualArea()
      .rotate([0, 0])
			.scale(210)
			.translate([width / 2, height / 2]);
		
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
      .style('fill', "#bcbcbc")
      .style('stroke', "#fff")
      .style('stroke-width', 1)
      
		});

    svg.selectAll('path.graticule')
      .data(d3.geoGraticule().lines())
      .enter()
      .append('path')
      .classed('graticule', true)
      .attr('d', path)
      .style('fill', 'none')
      .style('stroke', '#222')
      .style('stroke-width', 0.5)
      .style('stroke-opacity', 0.5)
      .lower();
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
