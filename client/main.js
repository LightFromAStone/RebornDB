const DEFAULT_PATH = 'http://localhost:8765'

function selectPokemon() {
   pkmnInfo =  this.id.split('_');
   sessionStorage.setItem('currentPokemonNumber', pkmnInfo[0]);
   sessionStorage.setItem('currentPokemonName', pkmnInfo[1]);
}

function displayPokedex() {
   axios.get(`${DEFAULT_PATH}/pokedex`)
      .then(res => {
         const dexHead = document.getElementById('pokedex-head');
         // console.log(res.data);
         for (let i = 0; i < res.data.length; i++) {
            const container = document.createElement('div');
            const pokemonCard = document.createElement('a');
            pokemonCard.href = 'dex-entry.html';
            pokemonCard.className = 'poke-card';
            pokemonCard.id = `${res.data[i].pokemon_base_id}_${res.data[i].pokemon_name}`;
            pokemonCard.addEventListener('click', selectPokemon);
            let pokeNum = res.data[i].pokemon_base_id;
            let prependNum = '';
            if (pokeNum < 10) { prependNum = '00'; }
            else if (pokeNum < 100) { prependNum = '0'; }
            pokemonCard.innerText = `${prependNum}${res.data[i].pokemon_base_id}. ${res.data[i].pokemon_name}`;
            container.appendChild(pokemonCard);
            dexHead.appendChild(container);
         }
      })
      .catch(err => console.log(err));
};

// const loadDex = document.getElementById('load-pokedex');
// loadDex.addEventListener('click', displayPokedex)

window.onload = displayPokedex;