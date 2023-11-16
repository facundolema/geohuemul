<script lang="ts">
	export let src: string;
	export let label: string;
  export let href: string;
	export let width: string = '24rem';
	export let height: string = '18rem';
	export let aspect_ratio: string = '4/3';
</script>

<div id="container" style="width: {width}; aspect-ratio: {aspect_ratio}">
	<div id="background" />
	<p id="label">{label}</p>
	<a id="link" href={href}>
		<img {src} alt={label} />
	</a>
</div>

<style>
	#container {
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;
	}

	#link,
	#container,
	#label,
  img {
		transition: all 0.2s ease-in-out;
	}

	#container:hover > #link {
		transform: translate(0, 10px);
	}

  #container:hover img {
    opacity: 0.7;
  }

	#container:hover > #label {
		visibility: visible;
		transform: scale(1) translateY(10px);
	}

	#label {
		position: absolute;
		text-align: center;
		padding: 0.25rem 1rem;
		font-size: 1.5rem;
		font-weight: 600;
		color: var(--light);
		background-color: var(--purple);
		border-radius: 0.5rem;
		visibility: hidden;
		z-index: 20;
		transform: scale(0);
		pointer-events: none;
    text-transform: capitalize;
	}

	#link {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		overflow: hidden;
		border-radius: 2rem;
		border: 5px solid var(--light);
		background-color: black;
		z-index: 10;
	}

	#background {
		position: absolute;
		top: 10px;
		width: 100%;
		height: 100%;
		background-color: var(--purple);
		border-radius: 2rem;
	}
</style>
