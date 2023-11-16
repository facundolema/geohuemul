<script lang="ts">
  export let title: string;
</script>

<h2 class="subtitle"><em>{title}</em></h2>

<style>
	.subtitle {
		animation-name: float;
		animation-duration: 1s;
		animation-delay: 1s;
		animation-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
		animation-fill-mode: forwards;
		transform: translateY(300px);
		font-size: 6rem;
	}
	
	@keyframes float {
		0% {
			transform: translatey(300px);
		}
		100% {
			transform: translatey(0px);
			font-size: 5rem;
		}
	
	}
</style>