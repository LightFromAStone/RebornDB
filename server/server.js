require('dotenv').config();
const express = require('express');
const app = express();
const cors = require('cors');
const {SERVER_PORT} = process.env;
const {
   getAllPokemon,
   getPokemonIdNumber,
   getPokemonName,
   getMainDexEntry,
   getPokemonAbilities
} = require('./controller.js');

app.use(express.json());
app.use(cors());

app.get('/pokedex', getAllPokemon);
app.get('/pokemonDexNum/:name', getPokemonIdNumber);
app.get('/pokemonName/:id', getPokemonName);
app.get('/dexEntry/:id', getMainDexEntry);
app.get('/pokemonAbilities/:id', getPokemonAbilities);


app.listen(SERVER_PORT, () => console.log(`up on ${SERVER_PORT}`))