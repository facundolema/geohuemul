<script lang="ts">
  export let slug: string;
	import SectionRect from '$components/SectionRect.svelte';
</script>

<div class="flex flex-col w-[55%] aspect-[7/4] gap-[25px]">
	<div class="flex gap-[25px] w-full flex-1">
		<div class="w-[61.5%] h-full">
			<SectionRect
			label="World"
			src="/thumb/north_america.png"
			href="/{slug}/world"
			width="100%"
			aspect_ratio="11/6.5"
			/>
		</div>
		<div class="flex-1 h-full flex flex-col gap-[25px]">
			<div class="w-full flex-1">
				<SectionRect
				label="Europe"
				src="/thumb/europe.png"
				href="/{slug}/europe"
				width="100%"
				aspect_ratio="6.5/3"
				/>
			</div>
			<div class="w-full flex-1">
				<SectionRect
				label="Africa"
				src="/thumb/africa.png"
				href="/{slug}/south_america"
				width="100%"
				aspect_ratio="6.5/3"
				/>
			</div>
		</div>
	</div>
	<div class="flex gap-[25px] w-full flex-[0.5]">
		<div class="flex-1 h-full">
			<SectionRect
			label="North America"
			src="/thumb/north_america.png"
			href="/{slug}/north_america"
			width="100%"
			aspect_ratio="4/3"
			/>
		</div>
		<div class="flex-1 h-full">
			<SectionRect
			label="South America"
			src="/thumb/south_america.png"
			href="/{slug}/south_america"
			width="100%"
			aspect_ratio="4/3"
			/>
		</div>
		<div class="flex-1 h-full">
			<SectionRect
			label="Asia"
			src="/thumb/asia.png"
			href="/{slug}/asia"
			width="100%"
			aspect_ratio="4/3"
			/>
		</div>
		<div class="flex-1 h-full">
			<SectionRect
			label="Oceania"
			src="/thumb/oceania.png"
			href="/{slug}/oceania"
			width="100%"
			aspect_ratio="4/3"
			/>
		</div>
	</div>
</div>