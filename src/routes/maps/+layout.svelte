<script>
  import { page } from '$app/stores'
</script>

{#if $page.url.pathname !== '/maps'}
  <div><slot/></div>
{:else}
  <slot/>
{/if}

<style>
  div {
    height: 100%;
    background-color: white;
  }
</style>