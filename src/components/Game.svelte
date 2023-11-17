<script lang="ts">
	export let mapath;
	export let filterfun = (feature) => true;
	import { onMount } from 'svelte';
	import { color } from '$lib/constants';
	import InputCard from '$components/InputCard.svelte';
	let L; let geojson;

	let guessed: Array<String> = [];
	let total = 200;
	let time = '00:00:00';
	let interval = null;

	function startTimer() {
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

	// Highlights the feature, adds it to the guessed array, and checks if the game is over
	// if the feature doesn't exist (incorrect guess), it returns false
	function select(guess: string): boolean {
		let selected: null | SVGPathElement = null;

		console.log(guess);

		document.querySelectorAll('path[type="departamento"]').forEach((path) => {
			let names = path.getAttribute('names');

			if (!names) {
				console.log('Error: no `names` attribute', path);
				return false;
			}

			if (JSON.parse(names).includes(guess.toLowerCase())) selected = path;
		});

		if (!selected) return false;

    if (selected.getAttribute('guessed') === 'true') return true;

		if (guessed.length === 0) startTimer();

		guessed = [...guessed, selected.getAttribute('id')];

    selected.style.fill = color.red;
    selected.setAttribute('guessed', 'true');

		// If the game is over, stop the timer
		if (guessed.length === geojson.features.length) {
			clearInterval(interval);
			interval = null;
		}

		return true;
	}

	function onkeyup(e: KeyboardEvent) {
		if (e.key === 'Enter' && e.target instanceof HTMLInputElement) {
			if (select(e.target.value)) {
				e.target.value = '';
			} else {
				e.target.offsetWidth;
				e.target.classList.add('error');
				setTimeout(() => e.target.classList.remove('error'), 500);
			}
		}
	}

	onMount(async () => {
		L = (await import('leaflet')).default;
		const map = L.map('map', {
			center: [-37.3, -60],
			zoom: 6.9,
			minZoom: 4.5,
			zoomSnap: 0.1
		});

		const response = await fetch(mapath);
		geojson = await response.json();
    geojson.features = geojson.features.filter(filterfun);
    total = geojson.features.length;
		L.geoJSON(geojson, {
			onEachFeature: (feature, layer) => {
				layer.bindPopup(feature.properties.NAM);
				layer.on('click', () => {
					layer.setStyle({
						color: '#000',
						fillColor: color.red,
						weight: 1.5,
						fillOpacity: 1
					});
				});
				layer.on('add', () => {
					layer._path.setAttribute('type', 'departamento');
					layer._path.setAttribute('names', JSON.stringify([feature.properties.NAM.toLowerCase()]));
					layer._path.setAttribute('id', feature.properties.NAM.toLowerCase());
				});
			},
			style: (feature) => {
				return {
					color: '#000',
					fillColor: color.beige,
					weight: 1.5,
					fillOpacity: 1
				};
			}
		}).addTo(map);
	});
</script>

<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
</svelte:head>

<main>
	<div class="cont">
		<div id="map" />
		<div class="card">
			<InputCard
				{onkeyup}
				height="fit-content"
				width="24rem"
				progress="{guessed.length}/{total} [{((guessed.length / total) * 100).toFixed(2)}%]"
				{time}
			/>
		</div>
	</div>
</main>

<style>
	main {
		height: 100%;
		width: 100vw;
		padding: 0;
		background-color: var(--light);
	}
	#map {
		height: 100%;
		width: 100%;
		border: 1px solid black;
		background-color: var(--ocean);
	}
	.cont {
		width: 100%;
		height: 100%;
		position: relative;
	}
	.card {
		position: absolute;
		bottom: 2rem;
		right: 2rem;
		z-index: 1000;
	}
</style>
