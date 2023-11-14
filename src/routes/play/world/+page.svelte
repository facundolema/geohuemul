<script lang="ts">
	import * as d3 from 'd3';
	import { onMount } from 'svelte';
	import { color } from '$lib/constants';

	let guessed: Array<String> = [];
	let total = 0;
	let start;
	let btn_label = 'Start';
	let time = '00:00:00';
	let interval = null;

	function startTimer() {
		btn_label = btn_label === 'Start' ? 'Stop' : 'Start';
		if (interval) {
			clearInterval(interval);
			interval = null;
		} else {
			let start = Date.now();
			interval = setInterval(() => {
				let delta = Date.now() - start;
				time = new Date(Math.floor(delta / 1000) * 1000).toISOString().slice(11, 19);
			}, 1000);
		}
	}

	function drawMap() {
		let container = d3.select('#map-container');
		let [width, height] = [container.node()?.clientWidth, container.node()?.clientHeight];

		let projection = d3
			.geoMercator()
			.scale(250)
			.center([0, 25])
			.translate([width / 2, height / 2]);

		let path = d3.geoPath().projection(projection);

		let svg = container
			.append('svg')
			.attr('width', width)
			.attr('height', height)
			.style('border', '1px solid #222')
			.style('background-color', '#caf0f8');

		let g = svg.append('g').attr('class', 'map');

		d3.json('/maps/UN_member_states.geojson').then(function (data) {
			total = data.features.length;
			g.selectAll('path')
				.data(data.features)
				.enter()
				.append('path')
				.attr('d', path)
				.style('fill', color.beige)
				.style('stroke', '#222')
				.style('stroke-width', 0.5);
		});
	}

	onMount(drawMap);

	function select(feature: string) {
		let selected = d3
			.selectAll('g.map path')
			.filter((country) =>
				country.properties.names.some((n) => n?.toLowerCase() === feature.toLowerCase())
			)
			.node();

		if (!exists(selected)) return;

		let path = d3.select(selected);

		if (path.attr('selected')) return;
		path.style('fill', color.red);
		path.attr('selected', true);

		if (guessed.length === 0) {
			startTimer();
		}
		guessed = [...guessed, path.attr('data-geounit')];
		if (guessed.length === 5) {
			clearInterval(interval);
			interval = null;
			btn_label = 'Start';
			document.querySelector('dialog').showModal();
		}
	}

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

	function onkeydown(e) {
		if (e.key === 'Enter') select(e.target.value);
	}
</script>

<dialog class="w-[50%] h-[50%] rounded-[1.5rem]">
<div class="w-full h-full flex flex-col
border-2 border-black justify-center items-center rounded-[1.5rem]
relative font-mono">

	<button class="bg-gray-300 rounded-full w-6 h-6 absolute top-[1rem] right-[1rem]"></button>
	<span class="flex flex-col justify-center items-center mb-8">
		<h1 class="text-4xl font-bold">You won!</h1>
		<p>in: {time}</p>
	</span>
	<span class="flex gap-2">
		<button class="bg-gray-300 px-4 py-2 border-2 border-black rounded-lg hover:bg-gray-400">Play again</button>
		<button class="bg-yellow-300 px-4 py-2 border-2 border-black rounded-lg hover:bg-yellow-400">Discover others</button>
	</span>
</div>
</dialog>

<div id="map-container">
	<div id="overlay">
		<div class="card font-mono flex flex-col gap-2">
			<h1 class="text-xl font-bold m-0 px-1">Can you name all the countries in the map?</h1>
			<p class="note">
				<b>country:</b> any of the 193 member states of the United Nations. Disputed territories are
				not showed.
			</p>
			<span />
			<input
				id="country-input"
				type="Search"
				placeholder="Add country by name"
				on:keydown={onkeydown}
				class="text-md"
			/>
			<span class="flex justify-between font-mono text-sm px-1">
				<span class="flex gap-2">
					<p>Guessed: {guessed.length}/{total}</p>
					<p>[{((guessed.length / total) * 100).toFixed(2)}%]</p>
				</span>
				<p>|</p>
				<p>Time: {time}</p>
			</span>
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
		width: 24rem;
	}

	input {
		border-radius: 8px;
		border: 1px solid #222;
		width: 100%;
		padding: 0.5rem;
		background-color: rgba(255, 255, 255, 0.35);
	}

	.note {
		font-size: 0.75rem;
		font-style: italic;
		font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
		background-color: rgb(240, 241, 144);
		border: 1px solid black;
		padding: 0.5rem;
		border-radius: 0.5rem;
		display: none;
	}

	:global(input.error):focus-visible {
		animation: shake 0.2s ease-in-out 0s 2;
		outline: 2px solid indianred;
	}

	@keyframes shake {
		0% {
			margin-left: 0rem;
		}
		25% {
			margin-left: 0.5rem;
		}
		75% {
			margin-left: -0.5rem;
		}
		100% {
			margin-left: 0rem;
		}
	}
</style>
