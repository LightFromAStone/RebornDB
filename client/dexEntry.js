const DEFAULT_PATH = 'http://localhost:8765'

let pokemonName = sessionStorage.getItem('currentPokemonName');
let pokemonNum = sessionStorage.getItem('currentPokemonNumber');

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

         const prevPage =  document.getElementById('prev-pkmn');
         prevPage.addEventListener('click', () => {
            sessionStorage.setItem('currentPokemonNumber', `${+strNum}`);
            sessionStorage.setItem('currentPokemonName', `${prevName}`);
            location.reload()
         })
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

         const nextPage =  document.getElementById('next-pkmn');
         nextPage.addEventListener('click', () => {
            sessionStorage.setItem('currentPokemonNumber', `${+strNum}`);
            sessionStorage.setItem('currentPokemonName', `${nextName}`);
            location.reload()
         })
      })
      .catch(err => console.log(err));
   }
}

function setMainPkmnData(pkmnId) {
   axios.get(`${DEFAULT_PATH}/dexEntry/${pkmnId}`)
      .then(res => {
         let {
            catch_rate, gender_rate, growth_type, hatch_steps, pokemon_id, pokemon_type_1, pokemon_type_2
         } = res.data[0];
      
         let types = document.getElementById('pkmn-types');
         types.innerHTML = `<span>${pokemon_type_1}</span>`;
         if (pokemon_type_2 !== null) {
            let type2 = document.createElement('span');
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
            })
            .catch(err => console.log(err));

         axios.get(`${DEFAULT_PATH}/pokemonStats/${pokemon_id}`)
         .then(res => {
               const { hp, attack, defense, speed, sp_attack, sp_defense } = res.data[0];
               let stats = document.getElementById('pkmn-stats');
               stats.innerHTML = `<ul><li>HP - ${hp}</li><li>Attack - ${attack}</li><li>Defense - ${defense}</li><li>Special Attack - ${sp_attack}</li><li>Special Defense - ${sp_defense}</li><li>Speed - ${speed}</li></ul>`;
            })
            .catch(err => console.log(err));

         axios.get(`${DEFAULT_PATH}/pokemonMoves/${pokemon_id}`)
         .then(res => {
            // console.log(res.data);
            let movesSection = document.getElementById('pkmn-moves');
            let levelMoves = document.createElement('div');
            levelMoves.id = 'moves-level';
            levelMoves.innerHTML = `<h3>Level Up Moves</h3>`
            let eggMoves = document.createElement('div');
            eggMoves.id = 'moves-egg';
            eggMoves.innerHTML = `<h3>Egg Moves</h3>`
            let tutorMoves = document.createElement('div');
            tutorMoves.id = 'moves-tutor';
            tutorMoves.innerHTML = `<h3>Tutor Moves</h3>`
            let machineMoves = document.createElement('div');
            machineMoves.id = 'moves-machine';
            machineMoves.innerHTML = `<h3>TM/HM Moves</h3>`

            for (let i = 0; i < res.data.length; i++) {
               let { learn_method, move_name, base_power, move_type, damage_category, accuracy, total_pp, effect_chance, move_description } = res.data[i];
      
               let move = document.createElement('div');
               move.className = 'pkmn-move'
               if (!isNaN(learn_method)) {
                  if (learn_method === '0') { learn_method = 'Evo.'; }
                  if (base_power === '0') { base_power = ' - '; }
                  move.innerHTML = `<span>${learn_method}</span><span>${move_name}</span><span>${move_type}</span><span>${damage_category}</span><span class='hidden move-add-info'><span>Base Power - ${base_power}</span><span>Accuracy - ${accuracy}</span><span>PP - ${total_pp}</span><span>Description - ${move_description}</span></span>`
                  levelMoves.appendChild(move);
               }
               movesSection.appendChild(levelMoves);
            }
            let hiddenButtons = document.querySelectorAll('.pkmn-move');
            for (let i = 0; i < hiddenButtons.length; i++) {
               hiddenButtons[i].addEventListener('click', () => {
                  let hiddenSpan = hiddenButtons[i].querySelector('.move-add-info');
                  hiddenSpan.classList.toggle('hidden');
               })
            }
         })
         .catch(err => console.log(err));

      })
      .catch(err => console.log(err));
}

function renderPokemonPage() {
   pokemonName = sessionStorage.getItem('currentPokemonName');
   pokemonNum = sessionStorage.getItem('currentPokemonNumber');

   document.querySelector('title').innerText = `RebornDB - ${pokemonName}`;
   
   let strPokemonNum = '' + pokemonNum;
   if (pokemonNum < 100) { strPokemonNum = formatPokemonNumber(pokemonNum) }
   let current = document.getElementById('current-pkmn');
   current.innerHTML = `<span>${pokemonName}</span><span>#${strPokemonNum}</span>`

   if (pokemonNum === '29') { pokemonName += ' (F)'; }
   else if (pokemonNum === '32') { pokemonName += ' (M)'; }
   let imagePath = '../ImageGallery/Pokedex/' + strPokemonNum + ' ' + pokemonName + '/Sugimori.png'
   let imgElem = document.getElementById('pkmn-profile-pic').firstElementChild;
   imgElem.src = imagePath;
   imgElem.alt = pokemonName;


   setPrevAndNext(pokemonNum);
   setMainPkmnData(pokemonNum);
};

let movesButton = document.getElementById('show-moves-btn');
movesButton.addEventListener('click', () => {
   document.getElementById('pkmn-moves').classList.toggle('hidden');
   if (movesButton.innerText === 'Show Moves') { movesButton.innerText = 'Hide Moves'; }
   else { movesButton.innerText = 'Show Moves'; }
}) 

window.onload = renderPokemonPage;