<script lang="ts">
	export let onkeyup: (e: KeyboardEvent) => void;
	export let width = '100%';
	export let height = '100%';
	export let title = 'Input Card';
	export let progress = '0/0 [0%]';
	export let time = '00:00:00';
	function onclick() {
		const input = document.querySelector('input');
		const enterEvent = new KeyboardEvent('keyup', { key: 'Enter' });
		input.dispatchEvent(enterEvent);
	}
</script>

<div class="card" style="width: {width}; height: {height}">
	<h1 class="input-card-title">{title}</h1>
	<div style="display: flex; gap: 4px;">
		<input id="country-input" type="text" placeholder="Add country by name" on:keyup={onkeyup} />
		<button id="add-country" on:click={onclick}>Add</button>
	</div>
	<span class="flex justify-between font-mono text-sm px-1">
		<p>Guessed: {progress}</p>
		<p>|</p>
		<p>Time: {time}</p>
	</span>
</div>

<style>
	.card {
		background-color: rgba(255, 255, 255, 0.25);
		border: 2px solid white;
		border-radius: 1rem;
		padding: 1rem;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}
	
	button {
		border-radius: 8px;
		border: 1px solid #222;
		padding: 0.5rem;
		background-color: rgba(255, 255, 255, 0.35);
	}

	.input-card-title {
		margin: 0;
		font-size: 1.5rem;
		font-family: 'Courier New', Courier, monospace;
	}

	input {
		border-radius: 8px;
		border: 1px solid #222;
		width: 100%;
		padding: 0.5rem;
		background-color: rgba(255, 255, 255, 0.35);
	}

  :global(input.error):focus-visible {
		animation: shake 0.2s ease-in-out 0s 2;
		outline: 2px solid var(--red);
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
