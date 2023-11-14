import { formatCurrency, formatNumber } from '$lib/functions';
import { global_population, global_gdp, global_land, color } from '$lib/constants';

export class Country {
  name = 'Union #1';
  population = 0;
  total_area = 0;
  land_area = 0;
  water_area = 0;
  gdp = 0;
  countries = 0;

  get display() {
    return {
      Name: this.name,
      Population: formatNumber(this.population),
      'Total area': formatNumber(this.total_area) + ' km2',
      GDP: formatCurrency(this.gdp * 1000000),
      'GDP per capita':
        this.gdp == 0 ? 0 : formatCurrency((this.gdp * 1000000) / this.population),
      '% of global pop.': ((this.population / global_population) * 100).toFixed(2) + '%',
      '% of world GDP': ((this.gdp / global_gdp) * 100).toFixed(2) + '%',
      "% of Earth's land": ((this.land_area / global_land) * 100).toFixed(2) + '%'
    };
  }

  reset() {
    this.name = 'Union #1';
    this.population = 0;
    this.total_area = 0;
    this.land_area = 0;
    this.water_area = 0;
    this.gdp = 0;
    this.countries = 0;
  }
}