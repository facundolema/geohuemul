<script lang='ts'>
  import Game from '$components/Game.svelte';
  import { page } from '$app/stores';
	const provincia = $page.url.pathname.split('/').at(-1);
	import { provincias } from '$lib/constants';
	let pid = provincias.find((p) => p.name === provincia)?.id;
	console.log(pid);
</script>

<Game 
  mapath='/maps/argentina/departamentos.geojson'
  filterfun={(feature) => feature.properties.pid === pid}
/>