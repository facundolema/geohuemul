<main class="flex flex-col justify-center gap-24 items-center w-full h-full">

	<div class="flex flex-wrap gap-24 justify-center items-center">
		<div class="container">
			<a href="/play/1" class="card">
				<img src="/thumb/maps.png" alt="Play Game #1"/>
			</a>
			<span class="label">Europe</span>
		</div>
		<div class="container">
			<a href="/play/1" class="card">
				<img src="/thumb/maps.png" alt="Play Game #1"/>
			</a>
			<span class="label">Europe</span>
		</div>
	</div>

</main>

<style>
	.container {
		width: 24rem;
		aspect-ratio: 4/3;
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;
	}

	.card {
		width: 24rem;
		aspect-ratio: 4/3;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		position: relative;
		box-shadow: 0 0 20px var(--purple);
		border: 2px solid var(--purple);
		border-radius: 2rem;
		overflow: hidden;
	}
	
	.label {
		position: absolute;
		height: 2rem;
		padding: 0 1rem;
		display: flex;
		justify-content: center;
		align-items: center;
		bottom: -1rem;
		background-color: black;
		color: var(--purple);
		border-radius: 0.5rem;
		border: 2px solid var(--purple);
		box-shadow: 0 0 20px var(--purple);
	}

	.card:hover {
		animation-name: pulse;
		animation-duration: 1s;
		animation-iteration-count: infinite;

	}

	@keyframes pulse {
		0% {
			box-shadow: 0 0 20px var(--purple);
			border: 2px solid var(--purple);
		}
		50% {
			box-shadow: 0 0 30px var(--purple);
			border: 2px solid #cac0ff;
		}
		100% {
			box-shadow: 0 0 20px var(--purple);
			border: 2px solid var(--purple);
		}
	}
</style>
