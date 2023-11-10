import '../static/world'

let wikidataId = 'Q44754'; // replace with your Wikidata ID
let url = `https://www.wikidata.org/wiki/Special:EntityData/${wikidataId}.json`;

fetch(url)
    .then(response => response.json())
    .then(data => {
        let claims = data.entities[wikidataId].claims;
        let populationClaims = claims['P1082'];
        if (populationClaims) {
            let population = populationClaims[populationClaims.length -1].mainsnak.datavalue.value.amount;
            console.log(population);
        } else {
            console.log('No population data available');
        }
    })
    .catch(error => console.error('Error:', error));