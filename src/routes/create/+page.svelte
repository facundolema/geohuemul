<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';

	import { downloadImage, downloadMap } from '$lib/functions';
	import { color } from '$lib/constants';
	import { Country } from '$lib/country';

	let country = new Country();

	function onClick() {
		let feature = d3.select(this);
		let d = feature.datum();

		switchSelection(d.properties.geounit);

	}

	function drawMap() {
		let container = d3.select('#map-container');
		let [width, height] = [container.node().clientWidth, container.node().clientHeight];
		
		let projection = d3
			.geoMercator()
			.scale(200)
			.translate([width / 2, height / 2]);
		
		let path = d3.geoPath().projection(projection);

		let svg = container
			.append('svg')
			.attr('width', width)
			.attr('height', height)
			.style('border', '1px solid #222')
			.style('background-color', '#caf0f8');

		let g = svg.append('g').attr('class', 'map');

		d3.json('/world.geojson').then(function (data) {
			g.selectAll('path')
				.data(data.features)
				.enter()
				.append('path')
				.attr('d', path)
				.attr('data', (d) => JSON.stringify(d.properties))
				.attr('data-geounit', (d) => d.properties.geounit)
				.style('fill', color.base)
				.style('stroke', '#222')
				.style('stroke-width', 0.5)
				.on('click', onClick);
		});
	}

	onMount(drawMap);

	function switchSelection(feature: string | null) {
		if (!feature) {
			let input = document.querySelector('#country-input');
			console.log(input)
			feature = input.value;
			//console.log(input.value)
			//input.value = '';
		}
		
		console.log(feature);
		let d = d3.select(`[data-geounit="${feature}"]`);
		let data = JSON.parse(d.attr('data'));
		
		if (!d) return;

		let selected = d.attr('selected')
		d.style('fill', selected ? color.base : color.selected);
		d.attr('selected', selected ? null : true);
		country.population 	+= selected ? -data.pop_est		 : data.pop_est;
		country.countries 	+= selected ? -1 							 : 1;
		country.gdp 				+= selected ? -data.gdp_md		 : data.gdp_md;
		country.total_area 	+= selected ? -data.total_area : data.total_area;
		country.land_area 	+= selected ? -data.land_area  : data.land_area;
		country.water_area 	+= selected ? -data.water_area : data.water_area;
		country = country;
	}

	function onkeydown(e) {
		if (e.key === 'Enter') {
			switchSelection(e.target.value);
			e.target.value = '';
			return;
		}
	}
</script>

<div id="map-container">
	<div id="overlay">
		<div class="card">
			<p style="margin:0;padding:0;font-size:1.25rem;font-weight:600;text-align:center;">
				GeoHuemul
			</p>
		</div>
		<div class="card">
			<h1 contenteditable spellcheck="false" bind:textContent={country.name} />
			<table>
				{#each Object.entries(country.display) as [key, value]}
					<tr>
						<td>{key}</td>
						<td>{value}</td>
					</tr>
				{/each}
			</table>
		</div>
		<div class="card">
			<div style="display:flex;gap: 4px;">
				<input
					id="country-input"
					type="Search"
					placeholder="Add country by name"
					on:keydown={onkeydown}
				/>
				<button id="add-country" on:click={() => switchSelection()}>Add</button>
			</div>
		</div>
		<div class="card">
			<button class="download-svg" on:click={downloadMap}>Download map</button>
			<button class="download-svg" on:click={downloadImage}>Download</button>
		</div>
	</div>
</div>

<style>
	#map-container {
		height: 100%;
		position: relative;
	}

	#overlay {
		position: absolute;
		bottom: 20px;
		left: 20px;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.card {
		background-color: rgba(255, 255, 255, 0.2);
		padding: 1rem;
		border-radius: 1rem;
		border: 2px solid white;
		color: #222 !important;
		box-shadow: 0 0 1rem rgba(0, 0, 0, 0.15);
		& button {
			color: #222;
			background-color: white;
			padding: 0.25rem 0.5rem;
			border-radius: 0.5rem;
			border: 1px solid #222;
			text-decoration: none;
		}
	}

	.card > h1 {
		margin: 1rem 0;
	}

	#country-input {
		border-radius: 8px;
		border: 1px solid #222;
		width: 100%;
		padding: 0.5rem;
		background-color: rgba(255, 255, 255, 0.35);
	}

	table {
		width: 100%;
	}

	table,
	td {
		border: 1px solid #222;
		border-collapse: collapse;
	}

	td {
		padding: 0.25rem 0.5rem;
	}
</style>
