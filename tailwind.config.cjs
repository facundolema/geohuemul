/** @type {import('tailwindcss').Config}*/
const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			colors: {
				"purple": "#8E82C9",
				"light-blue": "#70AFDB",
				"yellow": "#F5BF89",
				"green": "#75BDA5",
				"red": "#CC6666",
				"dark": "#1A1A1A"
			}
		}
	},

	plugins: []
};

module.exports = config;
