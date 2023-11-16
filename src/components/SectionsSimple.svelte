<script lang="ts">
  export let slug: string;
	import SectionRect from '$components/SectionRect.svelte';
</script>

<div class="flex flex-wrap w-[55%] gap-12 justify-center items-center">
  <SectionRect
    label="World"
    src="/thumb/world_crop.png"
    href="/{slug}/world"
    width="100%"
    aspect_ratio="16/9"
  />
	{#each ['north_america', 'europe', 'asia', 'south_america', 'africa', 'oceania'] as continent}
		<SectionRect
			label={continent.replace(/_/g, ' ')}
			src="/thumb/{continent}.png"
			href="/{slug}/{continent}"
      width="30%"
		/>
	{/each}
</div>