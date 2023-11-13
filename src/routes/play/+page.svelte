<main>
	<span
		class="flex gap-4 w-full self-start justify-self-start bg-yellow-300
    items-center justify-center py-2"
	>
		<img src="maintenance.svg" alt="maintenance" class="w-[1.5rem] h-[1.5rem]" />
		Exciting news! New games coming soon to this section. Stay tuned for a thrilling experience!
	</span>

	<div class="flex flex-wrap gap-6 justify-center items-center">
		<a
			href="/play/1"
			class=" w-[20%]
    flex flex-col justify-center items-center
    card relative"
		>
			<img src="/thumb/play_europe.png" alt="Play Game #1" class="object-contain rounded-[1rem]" />
			<span>Europe</span>
		</a>

		<a
			href="/play/1"
			class=" w-[20%]
  flex flex-col justify-center items-center
  card relative"
		>
			<img src="/thumb/play_europe.png" alt="Play Game #1" class="object-contain rounded-[1rem]" />
			<span>World</span>
		</a>
	</div>
</main>

<style>
	main {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 2rem;
	}

	.card img {
		box-shadow: 0 0 50px #8093f1c4;
		border: 2px solid #8093f1;
	}

	.card span {
		position: absolute;
		height: 2rem;
		padding: 0 1rem;
		display: flex;
		justify-content: center;
		align-items: center;
		bottom: -1rem;
		background-color: #8093f1;
		border-radius: 0.5rem;
		border: 2px solid white;
	}
</style>
