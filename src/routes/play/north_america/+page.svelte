<script lang="ts">
	import InputCard from '$components/InputCard.svelte';
	// import { getPaths } from '$lib/functions';

	import fs from 'fs';
	import path from 'path';

	export function get(p) {
  	const files = fs.readdirSync(p);
  	const directories = files.filter(file => fs.statSync(path.join(p, file)).isDirectory());
  	return directories
	}

	const directories = get('./src/routes/play/north_america/');
	console.log(directories);

	let guessed: Array<String> = [];
	let total = 200;
  let time = '00:00:00';
	let interval = null;

	function startTimer() {
		if (interval) {
			clearInterval(interval);
			interval = null;
		} else {
			let start = Date.now();
			interval = setInterval(() => {
				let delta = Date.now() - start;
				time = new Date(Math.floor(delta / 1000) * 1000).toISOString().slice(11, 19);
			}, 1000);
		}
	}

	function select(feature: string) {
    let selected = true

		if (!exists(selected)) return false;

		if (guessed.length === 0) {
			startTimer();
		}

		guessed = [...guessed, 'hello'];
		if (guessed.length === 5) {
			clearInterval(interval);
			interval = null;
		}
	}

	function exists(selected: boolean) {
		let input = document.querySelector('#country-input');
		if (selected) {
			input?.classList.remove('error');
			input.value = '';
			return true;
		} else {
			input?.classList.remove('error');
			input.offsetWidth;
			input?.classList.add('error');
			return false;
		}
	}

	function onkeydown(e) {
		if (e.key === 'Enter') select(e.target.value);
	}

</script>

<InputCard
  onkeyup={onkeydown}
  height='fit-content'
  width='24rem'
  progress="{guessed.length}/{total} [{((guessed.length / total) * 100).toFixed(2)}%]"
  time={time}
/>

<div style="color: white;">
  {time}
	{directories}
</div>