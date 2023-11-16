<div class="animated flex justify-center items-center">
  <slot/>
</div>

<style>
  .animated {
    animation-name: appear;
    animation-duration: 1s;
    animation-delay: 1s;
    animation-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
    animation-fill-mode: forwards;
    transform: scale(0);
  }

  @keyframes appear {
    0% {
      transform: scale(0);
      opacity: 0;
    }
    100% {
      transform: scale(1);
      opacity: 1;
    }
  }
</style>