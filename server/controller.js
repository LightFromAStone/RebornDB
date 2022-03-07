require('dotenv').config();
const Sequelize = require('sequelize');

const sequelize = new Sequelize(
    process.env.CONNECTION_STRING, {
        dialect: 'postgress',
        dialectOptions: {
            ssl: { rejectUnauthorized: false }
        }
    }
);

module.exports = {
   getAllPokemon: (req, res) => {
      sequelize.query(`SELECT pokemon_base_id, pokemon_name FROM pokemon_base`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getPokemonIdNumber: (req, res) => {
      sequelize.query(`SELECT pokemon_base_id FROM pokemon_base WHERE pokemone_name = ${req.params.name}`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getPokemonName: (req, res) => {
      sequelize.query(`SELECT pokemon_name FROM pokemon_base WHERE pokemon_base_id = ${req.params.id}`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getMainDexEntry: (req, res) => {
      sequelize.query(`SELECT a.gender_rate, a.growth_type, a.catch_rate, a.hatch_steps, b.pokemon_id, b.pokemon_type_1, b.pokemon_type_2 
      FROM pokemon_base AS a 
      JOIN pokemon AS b ON a.pokemon_base_id = b.pokemon_base_id 
      WHERE a.pokemon_base_id = ${req.params.id};`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },


//    SELECT name, employees.dept_code, departments.dept_code, dept
// FROM employees
//   JOIN departments
//     ON employees.dept_code = departments.dept_code;

   getPokemonAbilities: (req, res) => {
      sequelize.query(`SELECT abilities.ability_name, abilities.ability_description 
      FROM pokemon_abilities 
      JOIN abilities ON pokemon_abilities.ability_id = abilities.ability_id 
      WHERE pokemon_id = '${req.params.id}'`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getPokemonTypes: (req, res) => {

   },

   getPokemonStats: (req, res) => {

   },

   getEvolutions: (req, res) => {

   },

   getLevelMoves: (req, res) => {

   },

   getEggMoves: (req, res) => {

   },

   getMachineMoves: (req, res) => {

   },

   getTutorMoves: (req, res) => {

   }

};