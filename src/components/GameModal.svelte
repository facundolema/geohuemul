<script>
  export let time = '00:00:00';
</script>

<dialog class="w-[50%] h-[50%] rounded-[1.5rem]">
  <div class="w-full h-full flex flex-col
  border-2 border-black justify-center items-center rounded-[1.5rem]
  relative font-mono">
  
    <button class="bg-gray-300 rounded-full w-6 h-6 absolute top-[1rem] right-[1rem]"></button>
    <span class="flex flex-col justify-center items-center mb-8">
      <h1 class="text-4xl font-bold">You won!</h1>
      <p>in: {time}</p>
    </span>
    <span class="flex gap-2">
      <button class="bg-gray-300 px-4 py-2 border-2 border-black rounded-lg hover:bg-gray-400">Play again</button>
      <button class="bg-yellow-300 px-4 py-2 border-2 border-black rounded-lg hover:bg-yellow-400">Discover others</button>
    </span>
  </div>
</dialog>

<style>
  
</style>