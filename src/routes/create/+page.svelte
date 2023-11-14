<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';

	import { downloadImage, downloadMap } from '$lib/functions';
	import { color } from '$lib/constants';
	import { Country } from '$lib/country';
	import FaDownload from 'svelte-icons/fa/FaDownload.svelte';
	import FaFileDownload from 'svelte-icons/fa/FaFileDownload.svelte';
	import FaRegTimesCircle from 'svelte-icons/fa/FaRegTimesCircle.svelte';
	import IoMdColorFilter from 'svelte-icons/io/IoMdColorFilter.svelte';
	import DataTable from '$components/DataTable.svelte';
	import Input from '$components/Input.svelte';

	function exists(selected: d3.BaseType | null) {
		let input = document.querySelector('#country-input');
		if (selected) {
			input?.classList.remove('error');
			input.value = '';
			return true;
		} else {
			input?.classList.remove('error');
			input.offsetWidth;
			input?.classList.add('error');
			return false;
		}
	}

	let country = new Country();
	let selection = '';

	let color_s = color.red;

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
			.classed('map', true)
			.attr('width', width)
			.attr('height', height)
			.style('border', '1px solid #222')
			.style('background-color', color.ocean);

		let g = svg.append('g').attr('class', 'map');

		d3.json('/maps/world.geojson').then(function (data) {
			g.selectAll('path')
				.data(data.features)
				.enter()
				.append('path')
				.attr('d', path)
				.attr('data', (d) => JSON.stringify(d.properties))
				.attr('data-geounit', (d) => d.properties.geounit)
				.style('fill', color.beige)
				.style('stroke', '#222')
				.style('stroke-width', 0.5)
				.on('click', (e) => switchSelection(e.target.getAttribute('data-geounit')));
		});
	}

	onMount(drawMap);

	function switchSelection(feature: string) {
		let s: d3.Selection = d3
			.selectAll('g.map path')
			.filter((country) =>
				country.properties.names.some(
					(name: string) => name?.toLowerCase() === feature?.toLowerCase()
				)
			)
			.node();

		if (!exists(s)) return;

		let d: d3.Selection = d3.select(s);
		let data = JSON.parse(d.attr('data'));
		let selected = d.attr('selected');

		// Update country data
		d.style('fill', selected ? color.beige : color_s);
		d.attr('selected', selected ? null : true);
		country.population += selected ? -data.pop_est : data.pop_est;
		country.countries += selected ? -1 : 1;
		country.gdp += selected ? -data.gdp_md : data.gdp_md;
		country.total_area += selected ? -data.total_area : data.total_area;
		country.land_area += selected ? -data.land_area : data.land_area;
		country.water_area += selected ? -data.water_area : data.water_area;
		country = country;
	}

	function clearSelection() {
		country.reset();
		country = country;
		color_s = color.red;
		d3.selectAll('g.map path').style('fill', color.beige).attr('selected', null);
	}

	function onkeyup(e: KeyboardEvent) {
		selection = e.target?.value;
		if (e.key === 'Enter') switchSelection(selection);
	}

	const options = [
		{ action: 'Clear selection', fun: clearSelection, icon: FaRegTimesCircle },
		{ action: 'Download map', fun: downloadMap, icon: FaDownload },
		{ action: 'Download image', fun: downloadImage, icon: FaFileDownload }
	];
</script>

<div id="map-container">
	<div id="overlay">
		<!-- title Card -->
		<div class="card">
			<h2>GeoHuemul</h2>
		</div>

		<!-- Information Card -->
		<div class="card">
			<h1
				class="text-4xl font-bold"
				contenteditable
				spellcheck="false"
				bind:textContent={country.name}
			/>
			<DataTable data={country.display} />
		</div>

		<!-- Input Card -->
		<div class="card">
			<Input {onkeyup} />
		</div>

		<!-- Options Card -->
		<div class="card flex justify-end gap-2">
			<span id="color-picker-container">
				<span id="picker-icon"><IoMdColorFilter /></span>
				<input
					type="color"
					id="color-picker"
					value={color_s}
					on:change={(e) => (color_s = e.target.value)}
				/>
			</span>
			<span class="flex-grow" />
			{#each options as { action, fun, icon: Icon }}
				<button class="download-btn" on:click={fun} title={action}>
					<div class="icon">
						<Icon />
					</div>
				</button>
			{/each}
		</div>
	</div>
</div>

<style>
	#color-picker {
		height: 100%;
		width: 100%;
	}
	
	input[type="color"] {
		-webkit-appearance: none;
	}
	input[type="color"]::-webkit-color-swatch-wrapper {
		padding: 0;
	}
	input[type="color"]::-webkit-color-swatch {
		border: none;
	}

	#color-picker-container {
		height: 2rem;
		width: 3rem;
		display: flex;
		border-radius: 0.5rem;
		overflow: hidden;
		border: 1px solid #222;
		border-style: inset;
		box-sizing: content-box;
		position: relative;
	}

	.download-btn {
		height: 2rem;
		width: 2rem;
		border-radius: 0.5rem;
		border: 1px solid #222;
	}

	.icon {
		width: 1rem;
		height: 1rem;
		color: var(--dark);
	}

	#picker-icon {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		margin: auto;
		width: 1.5rem;
		height: 1.5rem;
		color: var(--dark);
		pointer-events: none;
	}

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
</style>
