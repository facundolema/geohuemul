import { Canvg } from 'canvg';
import html2canvas from 'html2canvas';
import * as d3 from 'd3';
// import fs from 'fs';

export const formatNumber = (n: number) => {
  return n.toLocaleString('en-US');
}

export const formatCurrency = (n: number) => {
  if (n === 0) return 0;
  let units = ['K', 'M', 'B', 'T'];
  let unit = Math.floor((n.toFixed(0).length - 1) / 3) * 3;
  let nStr = (n / (10 ** unit)).toFixed(2);
  let unitname = units[(unit - 3) / 3];
  return '$' + nStr + unitname;
}

// Download the map as a .png
export function downloadMap() {
	const canvas = document.createElement('canvas');
	const ctx = canvas.getContext('2d');

	Canvg.fromString(ctx, document.querySelector('svg.map').outerHTML).render();

	ctx.globalCompositeOperation = 'destination-over';
	ctx.fillStyle = '#caf0f8';
	ctx?.fillRect(0, 0, canvas.width, canvas.height);

	let download = document.createElement('a');
	download.href = canvas.toDataURL('image/png');
	download.download = 'map.png';
	download.click();
}

// Download a the map + cards as a .png
export function downloadImage() {
	// Make cards opaque and change the border
	// (transparency doesn't work well with html2canvas)
	let cards = d3
		.selectAll('.card')
		.style('background-color', 'white')
		.style('box-shadow', 'none')
		.style('border', '1px solid black');

	// Download the map
	html2canvas(document.body, {scale: 2}).then(function (canvas) {
		let url = canvas.toDataURL('image/png');
		let download = document.createElement('a');
		download.href = url;
		download.download = 'map.png';
		download.click();
	
		// Reset the cards to their original state
		cards
			.style('background-color', 'rgba(255, 255, 255, 0.2)')
			.style('box-shadow', 'rgba(0, 0, 0, 0.15)')
			.style('border', '2px solid white');
	});
}

export function getPaths(path) {
	let folders = fs.readdirSync(path);
	return folders;
}

export function toTitleCase(s: string) {
	return s.split('_').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')
}