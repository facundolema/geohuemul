<script lang="ts">
  export let slug: string;
	import SectionRect from '$components/SectionRect.svelte';
</script>

<div class="flex flex-wrap w-[75%] gap-12 justify-center items-center">
	{#each ['north_america', 'europe', 'asia', 'south_america', 'africa', 'oceania'] as continent}
		<SectionRect
			label={continent.replace(/_/g, ' ')}
			src="/thumb/{continent}.png"
			href="/{slug}/{continent}"
		/>
	{/each}
</div>
