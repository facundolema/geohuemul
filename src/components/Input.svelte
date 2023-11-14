<script lang="ts">
	export let onkeyup: (e: KeyboardEvent) => void;
	function onclick() {
		const input = document.querySelector('input');
		const enterEvent = new KeyboardEvent('keyup', { key: 'Enter' });
		input.dispatchEvent(enterEvent);
	}
</script>

<div style="display:flex;gap: 4px;">
	<input id="country-input" type="Search" placeholder="Add country by name" on:keyup={onkeyup} />
	<button id="add-country" on:click={onclick}>Add</button>
</div>

<style>
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
