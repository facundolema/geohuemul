<script>
  import SectionsSimple from "$components/SectionsSimple.svelte";
  import SectionTitle from "$components/SectionTitle.svelte";
  import AnimatedWrapper from "$components/AnimatedWrapper.svelte";
</script>

<main>
	<SectionTitle title="Map Collection"/>
  <AnimatedWrapper>
    <SectionsSimple slug="maps"/>
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