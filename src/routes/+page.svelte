<script>
	import Section from '$components/Section.svelte';
  import FaBitcoin from 'svelte-icons/fa/FaBitcoin.svelte'
  import FaInstagram from 'svelte-icons/fa/FaInstagram.svelte'
  import FaTwitter from 'svelte-icons/fa/FaTwitter.svelte'
  import FaPaypal from 'svelte-icons/fa/FaPaypal.svelte'
  import FaDonate from 'svelte-icons/fa/FaDonate.svelte'
  import FaGithub from 'svelte-icons/fa/FaGithub.svelte'

  const social = [
    {"component": FaGithub, "href": "https://github.com/facundolema"},
    {"component": FaTwitter, "href": "https://twitter.com/geohuemul"},
    {"component": FaInstagram, "href": "https://instagram.com/geohuemul"},
  ]

  const donations = [
    {"component": FaBitcoin, "href": "/"},
    {"component": FaPaypal, "href": "/"},
    {"component": FaDonate, "href": "/"},
  ]
</script>

<div id="body">
	<main>
		<h1 class="title"><em>Geo</em>Huemul</h1>
		<div class="flex justify-center items-center gap-8">
			<Section label="Maps" src="/thumb/europe.png" />
			<Section label="Play" src="/thumb/asia.png" />
			<Section label="Create" src="/thumb/africa.png" />
		</div>
	</main>
	<footer>
    <span class="flex items-center justify-center gap-2">
      {#each social as {component: Icon, href}}
      <a href={href} class="icon">
        <Icon />
      </a>
      {/each}
    </span>
    <span>|</span>
    <span>Created by <em>Volfram Studio</em></span>
    <span>|</span>
		<span class="flex items-center justify-center gap-2">
      {#each donations as {component: Icon, href}}
        <a href={href} class="icon">
          <Icon />
        </a>
      {/each}
    </span>
  </footer>
	<div id="decoration" />
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

	#body {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
	}

	main {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex-grow: 1;
	}

	footer {
		width: 100%;
		height: 3rem;
		display: flex;
		gap: 1rem;
		justify-content: center;
		align-items: center;
		color: var(--light);
    font-size: large;
	}

	#decoration {
		width: 40%;
		height: 5px;
    border-radius: 50px 50px 0 0;
    align-self: center;
		background-image: linear-gradient(0deg, var(--purple), var(--light-blue));
	}

  .icon {
    width: 1.25rem;
    height: 1.25rem;
  }
</style>
