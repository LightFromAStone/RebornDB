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
      sequelize.query(`SELECT * FROM pokemon`)
      .then(dbRes => res.status(200).send(dbRes[0]))
      .catch(err => console.log(err))
   }
};