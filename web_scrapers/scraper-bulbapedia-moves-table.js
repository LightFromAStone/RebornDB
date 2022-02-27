const Nightmare = require('nightmare');
const nightmare = Nightmare();

let selector = 'h6';
// let URL = process.argv[2];
// let search_name = process.argv[3];
nightmare
  .goto('https://bulbapedia.bulbagarden.net/wiki/Vulpix_(Pok%C3%A9mon)/Generation_VII_learnset#By_leveling_up')
  .wait(2000)
  .evaluate(selector => {
     let resultsArray = [];
     let data = [];
     let allTables = document.querySelectorAll(selector);
     let neededTables = [];
     for (let i = 0; i < allTables.length; i++) {
        if (allTables[i].firstChild.innerText != null && allTables[i].firstChild.innerText === 'Alolan Vulpix') { neededTables.push(allTables[i]); }
     }

   for (let i = 0; i < 4; i++) {
      let movesTable = neededTables[i].nextElementSibling;
      let body = movesTable.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.nextElementSibling;
      if(i === 0) {         
         for (tr of body.querySelectorAll('tr')) {
            let first = tr.firstElementChild;
            resultsArray.push(first.innerText);
            let second = first.nextElementSibling;
            let moveName = '';
            if (second.querySelector('b') != null) {
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
            if (third.querySelector('b') != null) {
               moveName = third.firstElementChild.firstElementChild.firstElementChild.innerText;
            }
            else {
               moveName = third.firstElementChild.firstElementChild.innerText;
            }
            resultsArray.push(moveName);
         }
      }
      else if (i === 2) {
         for (tr of body.querySelectorAll('tr')) {
            let second = tr.firstElementChild.nextElementSibling;
            let moveName = '';
            if (second.querySelector('b') != null) {
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
            if (second.querySelector('b') != null) {
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
  }, selector)
  .end()
  .then(text => console.log(text))
  .catch(error => {
    console.error('Failed:', error)
  })
