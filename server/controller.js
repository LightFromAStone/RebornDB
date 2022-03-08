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

   getPokemonAbilities: (req, res) => {
      sequelize.query(`SELECT abilities.ability_name, abilities.ability_description 
      FROM pokemon_abilities 
      JOIN abilities ON pokemon_abilities.ability_id = abilities.ability_id 
      WHERE pokemon_id = '${req.params.id}'`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getPokemonStats: (req, res) => {
      sequelize.query(`SELECT hp, attack, defense, speed, sp_attack, sp_defense 
      FROM base_stats WHERE pokemon_id = '${req.params.id}'`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getEvolutions: (req, res) => {

   },

   getPokemonMoves: (req, res) => {
      sequelize.query(`SELECT a.learn_method, b.move_name, b.base_power, b.move_type, b.damage_category, b.accuracy, b.total_pp, b.effect_chance, b.move_description 
      FROM pokemon_moves AS a 
      JOIN moves AS b ON a.move_id = b.move_id 
      WHERE a.pokemon_id = '${req.params.id}'`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   getFeedback: (req, res) => {
      sequelize.query(`SELECT feedback_name, feedback_content FROM feedback`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   },

   addFeedback: (req, res) => {
      let {name, content} = req.body;
      sequelize.query(`INSERT INTO feedback (feedback_name, feedback_content) 
      VALUES
      ('${name}', '${content}');`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   }

};