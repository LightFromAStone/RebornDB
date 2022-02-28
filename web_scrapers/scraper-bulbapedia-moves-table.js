const {matchMove} = require('./moves-array.js')

const pokesToGet = ['Rattata', 'Raticate', 'Raichu', 'Sandshrew', 'Sandslash', 'Vulpix', 'Ninetales', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Geodude', 'Graveler', 'Golem', 'Grimer', 'Muk', 'Exeggutor', 'Marowak'];


async function getMoves(pkmn) {
   const Nightmare = require('nightmare');
   const nightmare = Nightmare();
   const fs = require('fs');

   let selector = 'h6';

   let URL = `https://bulbapedia.bulbagarden.net/wiki/${pkmn}_(Pok%C3%A9mon)/Generation_VII_learnset#By_leveling_up`;
   let searchName = `Alolan ${pkmn}`;

   await nightmare
   .goto(URL)
   .wait(2000)
   .evaluate((selector, searchName) => {
      let resultsArray = [];
      let data = [];
      let allTables = document.querySelectorAll(selector);
      let neededTables = [];
      for (let i = 0; i < allTables.length; i++) {
         if (allTables[i].firstChild.innerText != null && allTables[i].firstChild.innerText === searchName) { neededTables.push(allTables[i]); }
      }
      if (typeof neededTables === 'undefined' || neededTables.length < 4) { return `Could not find tables for ${searchName}`; }

      for (let i = 0; i < 4; i++) {
         let movesTable = neededTables[i].nextElementSibling;
         let body = movesTable.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.nextElementSibling;
         let excpetions = ['Alolan Raichu', 'Alolan Exeggutor', 'Alolan Marowak'];
         if (i=== 2 && excpetions.includes(searchName)) { i++; data.push(['reference']); }
         if(i === 0) {         
            for (tr of body.querySelectorAll('tr')) {
               let first = tr.firstElementChild;
               resultsArray.push(first.innerText);
               let second = first.nextElementSibling;
               let moveName = '';
               // if (second.querySelector('b') != null) {
               if (second.firstElementChild.tagName === 'B') {
                  moveName = second.firstElementChild.firstElementChild.firstElementChild.innerText;
               }
               else {
                  moveName = second.firstElementChild.firstElementChild.innerText;
               }
               resultsArray.push(moveName);
            }
         }
         else if (i === 1) {
            for (tr of body.querySelectorAll('tr')) {
               let third = tr.firstElementChild.nextElementSibling.nextElementSibling;
               let moveName = '';
               // if (third.querySelector('b') != null) {
               if (third.firstElementChild.tagName === 'B') {
                  moveName = third.firstElementChild.firstElementChild.firstElementChild.innerText;
               }
               else {
                  moveName = third.firstElementChild.firstElementChild.innerText;
               }
               resultsArray.push(moveName);
            }
         }
         else if (i === 2) {
            // let excpetions = ['Alolan Raichu', 'Alolan Exeggutor', 'Alolan Marowak'];
            // if (excpetions.includes(searchName)) { data.push(['']); continue; }
            for (tr of body.querySelectorAll('tr')) {
               let second = tr.firstElementChild.nextElementSibling;
               let moveName = '';
               // if (second.querySelector('b') != null) {
               if (second.firstElementChild.tagName === 'B') {
                  moveName = second.firstElementChild.firstElementChild.firstElementChild.innerText;
               }
               else {
                  moveName = second.firstElementChild.firstElementChild.innerText;
               }
               resultsArray.push(moveName);
            }
         }
         else if (i === 3) {
            for (tr of body.querySelectorAll('tr')) {
               let second = tr.querySelector('td')
               let moveName = '';
               // if (second.querySelector('b') != null) {
               if (second.firstElementChild.tagName === 'B') {
                  moveName = second.firstElementChild.firstElementChild.firstElementChild.innerText;
               }
               else {
                  moveName = second.firstElementChild.firstElementChild.innerText;
               }
               resultsArray.push(moveName);
            }
         }
         data.push(resultsArray);
         resultsArray = [];
      }
      return data;
   }, selector, searchName)
   .end()
   .then(data => {
         let pokeCap = searchName.slice(7, searchName.length);
         pokeCap = pokeCap.toUpperCase();
         let writeData = `${searchName}\nALO${pokeCap}\nLevel Up:\n`;
         for(let i = 0; i < data[0].length; i++) {
            if (data[0][i] === 'Evo.') { writeData += '0,'; }
            else if (+data[0][i]) { writeData += `${data[0][i]},`; }
            else { writeData += `${matchMove(data[0][i])},`}
         }
         writeData = writeData.slice(0, -1);
         writeData += '\nTM:\n';
         for(let i = 0; i < data[1].length; i++) {
            writeData += `${matchMove(data[1][i])},`;
         }
         writeData = writeData.slice(0, -1);
         writeData += '\nBreeding:\n';
         if(data[2][0] != 'reference') {
            for(let i = 0; i < data[2].length; i++) {
               writeData += `${matchMove(data[2][i])},`
            }
            writeData = writeData.slice(0, -1);
         }
         writeData += '\nTutoring:\n';
         for(let i = 0; i < data[3].length; i++) {
            writeData += `${matchMove(data[3][i])},`
         }
         writeData = writeData.slice(0, -1);
         writeData += '\n\n';
         fs.appendFile('alolan-move-data.txt', writeData, err => {if(err) {console.log(err)}});
   })
   .catch(error => {
      console.error(`Failed on ${searchName}`, error)
   })
}

for (p = 0; p < pokesToGet.length; p++) {
   getMoves(pokesToGet[p]);
}
