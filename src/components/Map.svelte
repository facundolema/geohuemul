<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';

  export let projection: d3.GeoConicProjection | d3.GeoProjection;
  export let width: number;
  export let height: number;
  export let data: any;
  export let graticule: boolean = false;
  export let border: string = "#fff";

	function drawMap() {
		let container = d3.select('#map-container');
		let path = d3.geoPath().projection(projection);

		let svg = container
			.append('svg')
			.attr('width', width)
			.attr('height', height)
      .attr('xlmns', 'http://www.w3.org/2000/svg')
      .attr('xmlns:xlink', "http://www.w3.org/1999/xlink")

		let g = svg.append('g').attr('class', 'map');
    
    g.selectAll('path')
      .data(data)
      .enter()
      .append('path')
      .attr('d', path)
      .style('fill', (d) => Math.random() > 0.5 ? "#70AFDB" : "#8E82C9")
      .style('stroke', "#000")
      .style('stroke-width', 1)

    if (graticule) {
      svg.selectAll('path.graticule')
        .data(d3.geoGraticule().lines())
        .enter()
        .append('path')
        .classed('graticule', true)
        .attr('d', path)
        .style('fill', 'none')
        .style('stroke', '#333')
        .style('stroke-width', 1)
        .lower();
    }
  }

	onMount(drawMap);

</script>

<div id="map-container" style="height: {height}; width: {width}; border: 1px solid {border};"/>