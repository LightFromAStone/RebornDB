CREATE TABLE pokemon (
   pokemon_id SERIAL PRIMARY KEY,
   pokemon_name VARCHAR(50) NOT NULL,
   pokemon_text_id VARCHAR(50) NOT NULL,
   type1 VARCHAR(20) NOT NULL,
   type2 VARCHAR(20),
   gender_rate VARCHAR(30) NOT NULL,
   growth_rate VARCHAR(30) NOT NULL,
   catch_rate INT NOT NULL,
   hatch_steps INT NOT NULL
);

CREATE TABLE effort_points (
   effort_points_id SERIAL PRIMARY KEY,
   pokemon_id INT NOT NULL REFERENCES pokemon(pokemon_id),
   ev_hp INT NOT NULL,
   ev_attack INT NOT NULL,
   ev_defense INT NOT NULL,
   ev_sp_attack INT NOT NULL,
   ev_sp_defense INT NOT NULL,
   ev_speed INT NOT NULL
);

CREATE TABLE base_stats (
   base_stats_id SERIAL PRIMARY KEY,
   pokemon_id INT NOT NULL REFERENCES pokemon(pokemon_id),
   hp INT NOT NULL,
   attack INT NOT NULL,
   defense INT NOT NULL,
   sp_attack INT NOT NULL,
   sp_defense INT NOT NULL,
   speed INT NOT NULL
);

CREATE TABLE abilities (
   ability_id SERIAL PRIMARY KEY,
   ability_text_id VARCHAR(30) NOT NULL,
   ability_name VARCHAR(30) NOT NULL,
   ability_description VARCHAR(500)
);

CREATE TABLE pokemon_abilities (
   pkmn_ability_id SERIAL PRIMARY KEY,
   pokemon_id INT NOT NULL REFERENCES pokemon(pokemon_id),
   ability_id INT NOT NULL REFERENCES abilities(ability_id),
   is_hidden BOOLEAN NOT NULL
);

CREATE TABLE evolutions (
   evolution_id SERIAL PRIMARY KEY,
   pokemon_id INT NOT NULL REFERENCES pokemon(pokemon_id),
   evolves_into INT NOT NULL REFERENCES pokemon(pokemon_id),
   evolution_method VARCHAR(100)
);

CREATE TABLE function_code (
   function_code_id SERIAL PRIMARY KEY,
   function_code_value CHAR(3) NOT NULL,
   function_code_description VARCHAR(500)
);

CREATE TABLE moves (
   move_id SERIAL PRIMARY KEY,
   move_text_id VARCHAR(50) NOT NULL,
   move_name VARCHAR(50) NOT NULL,
   function_code_id INT NOT NULL REFERENCES function_code(function_code_id),
   base_power INT NOT NULL,
   move_type VARCHAR(20) NOT NULL,
   damage_category VARCHAR(20) NOT NULL,
   accuracy INT NOT NULL,
   total_pp INT NOT NULL,
   effect_chance INT NOT NULL,
   target VARCHAR(50) NOT NULL,
   priority INT NOT NULL,
   move_description VARCHAR(500) NOT NULL
);

CREATE TABLE pokemon_moves (
   pokemon_moves_id SERIAL PRIMARY KEY,
   pokemon_id INT NOT NULL REFERENCES pokemon(pokemon_id),
   move_id INT NOT NULL REFERENCES moves(move_id),
   learn_method VARCHAR(50) NOT NULL
);

CREATE TABLE flags (
   flag_id SERIAL PRIMARY KEY,
   flag_value CHAR(1),
   flag_description VARCHAR(100)
);

CREATE TABLE move_flags (
   move_flag_id SERIAL PRIMARY KEY,
   move_id INT NOT NULL REFERENCES moves(move_id),
   flag_id INT NOT NULL REFERENCES flags(flag_id)
);

CREATE TABLE egg_groups (
   egg_group_id SERIAL PRIMARY KEY,
   egg_group_name VARCHAR(20) NOT NULL
);

CREATE TABLE pokemon_egg_groups (
   pokemon_egg_group_id SERIAL PRIMARY KEY,
   pokemon_id INT NOT NULL REFERENCES pokemon(pokemon_id),
   egg_group_id INT NOT NULL REFERENCES egg_groups(egg_group_id)
);
