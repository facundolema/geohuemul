<script lang="ts">
  export let data: { [key: string]: string | number } = {};
</script>

<table>
  {#each Object.entries(data) as [key, value]}
    <tr>
      <td>{key}</td>
      <td>{value}</td>
    </tr>
  {/each}
</table>


<style>
  table {
		width: 100%;
	}

	table,
	td {
		border: 1px solid #222;
		border-collapse: collapse;
	}

	td {
		padding: 0.25rem 0.5rem;
	}
</style>