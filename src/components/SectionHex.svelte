<script lang="ts">
	export let src: string;
	export let label: string;
</script>

<div>
  <a href="/{label.toLowerCase()}">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="300" height="300" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <pattern id="image-bg" x="0" y="0" height="300" width="300" patternUnits="userSpaceOnUse">
          <image width="300" height="300" xlink:href={src}></image>
        </pattern>
      </defs>
      <polygon points="150,300 20,225 20,75 150,0 280,75 280,225" fill="url('#image-bg')"
        transform="scale(0.95) translate(7.5, 7.5)"
      />
    </svg>
	</a>
</div>

<style>
	div {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 300px;
    height: 300px;
	}
  polygon {
    stroke: var(--purple);
    stroke-width: 5px;
  }
</style>
