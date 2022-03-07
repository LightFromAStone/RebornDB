const DEFAULT_PATH = 'http://localhost:8765'

function formatPokemonNumber(num) {
   if (num < 10) { return '00' + num; }
   else return '0' + num;
}

function setPrevAndNext(currentNum) {
   if (currentNum !== 1) {
      const prevNum = +currentNum - 1;
      let prevName = '';
      let strNum = '' + prevNum;
      if (prevNum < 100) { strNum = formatPokemonNumber(prevNum)}

      axios.get(`${DEFAULT_PATH}/pokemonName/${prevNum}`)
      .then(res => {
         prevName = res.data[0].pokemon_name
         let previous = document.getElementById('prev-pkmn');
         previous.innerHTML = `<span><</span><span>#${strNum}</span><span>${prevName}</span>`
      })
      .catch(err => console.log(err));

   }
   if (currentNum !== 807) {
      const nextNum = +currentNum + 1;
      let nextName = '';
      let strNum = '' + nextNum;
      if (nextNum < 100) { strNum = formatPokemonNumber(nextNum); }

      axios.get(`${DEFAULT_PATH}/pokemonName/${nextNum}`)
      .then(res => {
         nextName = res.data[0].pokemon_name;
         let next = document.getElementById('next-pkmn');
         next.innerHTML = `<span>${nextName}</span><span>#${strNum}</span><span>></span>`
      })
      .catch(err => console.log(err));
   }
}

function setMainPkmnData(pkmnId) {
   axios.get(`${DEFAULT_PATH}/dexEntry/${pkmnId}`)
      .then(res => {
         console.log(res.data);
         let {
            catch_rate, gender_rate, growth_type, hatch_steps, pokemon_id, pokemon_type_1, pokemon_type_2
         } = res.data[0];
      
         let types = document.getElementById('pkmn-types');
         types.innerHTML = `<div>${pokemon_type_1}</div>`;
         if (pokemon_type_2 !== null) {
            let type2 = document.createElement('div');
            type2.innerText = pokemon_type_2;
            types.appendChild(type2);
         }

         let generalInfo = document.getElementById('general-info');
         generalInfo.innerHTML = `<ul><li>Gender Rate: ${gender_rate}</li><li>Catch Rate: ${catch_rate}</li><li>Growth Type: ${growth_type}</li><li>Steps to Hatch: ${hatch_steps}</li></ul>`

         axios.get(`${DEFAULT_PATH}/pokemonAbilities/${pokemon_id}`)
            .then(res => {
               abilitySection = document.getElementById('pkmn-abilities');
               abilitySection.appendChild(document.createElement('ul'));
               for (let i = 0; i < res.data.length; i++) {
                  let ability = document.createElement('li');
                  ability.innerText = res.data[i].ability_name;
                  abilitySection.firstElementChild.appendChild(ability);
               }
               console.log(res.data);
            })
            .catch(err => console.log(err));
      })
      .catch(err => console.log(err));
}

function renderPokemonPage() {
   let pokemonName = sessionStorage.getItem('currentPokemonName');
   let pokemonNum = sessionStorage.getItem('currentPokemonNumber');
   
   let strPokemonNum = '' + pokemonNum;
   if (pokemonNum < 100) { strPokemonNum = formatPokemonNumber(pokemonNum) }
   let current = document.getElementById('current-pkmn');
   current.innerHTML = `<span>${pokemonName}</span><span>#${strPokemonNum}</span>`

   setPrevAndNext(pokemonNum);
   setMainPkmnData(pokemonNum);
};

window.onload = renderPokemonPage;