<script>
	import SectionsSimple from "$components/SectionsSimple.svelte";
	import SectionTitle from "$components/SectionTitle.svelte";
	import AnimatedWrapper from "$components/AnimatedWrapper.svelte";
</script>

<main>
	<SectionTitle title="Play. Learn. Have fun!" />
	<AnimatedWrapper>
		<SectionsSimple slug="play"/>
	</AnimatedWrapper>
</main>

<style>
	main {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 4rem;
		padding: 4rem;
	}
</style>