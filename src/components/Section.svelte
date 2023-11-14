<script lang="ts">
	export let src: string;
	export let label: string;
</script>

<div id="container">
  <p id="label">{label}</p>
	<a id="link" href="/{label.toLowerCase()}">
		<img {src} alt={label} />
	</a>
</div>

<style>  
  #container {
    width: 14rem;
		height: 14rem;
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;
    box-shadow: 0 8px 0 var(--purple);
		border: 5px solid var(--light);
    border-radius: 50%;
		overflow: hidden;
	}

  #link, #container, #label {
    transition: all 0.2s ease-in-out;
  }
  
  #container:hover {
    transform: translate(0, 4px);
    box-shadow: none;
  }

  #container:hover > #link {
    opacity: 0.7;
  }

  #container:hover > #label {
    visibility: visible;
    transform: scale(1);
  }

  #link {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #label {
    position: absolute;
    text-align: center;
    padding: 0.25rem 1rem;
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--light);
    background-image: linear-gradient(90deg, var(--purple), var(--light-blue));
    border-radius: 0.5rem;
    visibility: hidden;
    z-index: 10;
    transform: scale(0);
    pointer-events: none;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>
