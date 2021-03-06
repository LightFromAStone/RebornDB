CREATE TYPE EXPGROWTH AS ENUM ('Erratic', 'Fast', 'Medium Fast', 'Medium Slow', 'Slow', 'Fluctuating');
CREATE TYPE MOVECLASS AS ENUM ('Physical', 'Special', 'Status');
CREATE TYPE POCKET AS ENUM ('Items', 'Medicine', 'Poke Balls', 'TMs & HMs', 'Berries', 'Mail', 'Battle Items', 'Key Items');

CREATE TABLE pokemon_type (
   pokemon_type_id VARCHAR(20) PRIMARY KEY
);

CREATE TABLE in_battle_use (
   in_battle_use_id SERIAL PRIMARY KEY,
   useability_definition VARCHAR(300) NOT NULL
);

CREATE TABLE out_battle_use (
   out_battle_use_id SERIAL PRIMARY KEY,
   useability_definition VARCHAR(300) NOT NULL
);

CREATE TABLE special_items_use (
   special_items_use_id SERIAL PRIMARY KEY,
   useability_definition VARCHAR(300) NOT NULL
);

CREATE TABLE game_items (
   game_item_id VARCHAR(30) PRIMARY KEY,
   game_item_name VARCHAR(30) NOT NULL,
   bag_pocket POCKET NOT NULL,
   game_item_price INT NOT NULL,
   game_item_description VARCHAR(200) NOT NULL,
   in_battle_use_id INT NOT NULL REFERENCES in_battle_use(in_battle_use_id),
   out_battle_use_id INT NOT NULL REFERENCES out_battle_use(out_battle_use_id),
   special_items_use_id INT NOT NULL REFERENCES special_items_use(special_items_use_id)
);

CREATE TABLE pokemon_base (
   pokemon_base_id SERIAL PRIMARY KEY,
   pokemon_name VARCHAR(50) NOT NULL,
   gender_rate NUMERIC(4, 3) NOT NULL,
   growth_type EXPGROWTH NOT NULL,
   catch_rate INT NOT NULL,
   hatch_steps INT NOT NULL
);

CREATE TABLE pokemon (
   pokemon_id VARCHAR(50) PRIMARY KEY,
   pokemon_base_id INT NOT NULL REFERENCES pokemon_base(pokemon_base_id),
   pokemon_type_1 VARCHAR(20) NOT NULL REFERENCES pokemon_type(pokemon_type_id),
   pokemon_type_2 VARCHAR(20) REFERENCES pokemon_type(pokemon_type_id)
);

CREATE TABLE wild_held_items (
   wild_held_item_id SERIAL PRIMARY KEY,
   game_item_id VARCHAR(30) NOT NULL REFERENCES game_items(game_item_id),
   pokemon_id VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   held_chance NUMERIC(3,2) NOT NULL
);

CREATE TABLE effort_points (
   effort_points_id SERIAL PRIMARY KEY,
   pokemon_id VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   ev_hp INT NOT NULL,
   ev_attack INT NOT NULL,
   ev_defense INT NOT NULL,
   ev_speed INT NOT NULL,
   ev_sp_attack INT NOT NULL,
   ev_sp_defense INT NOT NULL
);

CREATE TABLE base_stats (
   base_stats_id SERIAL PRIMARY KEY,
   pokemon_id VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   hp INT NOT NULL,
   attack INT NOT NULL,
   defense INT NOT NULL,
   speed INT NOT NULL,
   sp_attack INT NOT NULL,
   sp_defense INT NOT NULL
);

CREATE TABLE abilities (
   ability_id VARCHAR(30) PRIMARY KEY,
   ability_name VARCHAR(30) NOT NULL,
   ability_description VARCHAR(500)
);

CREATE TABLE pokemon_abilities (
   pkmn_ability_id SERIAL PRIMARY KEY,
   pokemon_id VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   ability_id VARCHAR(30) NOT NULL REFERENCES abilities(ability_id),
   is_hidden BOOLEAN NOT NULL
);

CREATE TABLE evolutions (
   evolution_id SERIAL PRIMARY KEY,
   pokemon_id VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   evolves_into VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   evolution_method VARCHAR(100) NOT NULL,
   evolution_method_param VARCHAR(50)
);

CREATE TABLE function_codes (
   function_code_id CHAR(3) PRIMARY KEY,
   function_code_description VARCHAR(1500)
);

CREATE TABLE moves (
   move_id VARCHAR(50) PRIMARY KEY,
   move_name VARCHAR(50) NOT NULL,
   function_code_id CHAR(3) NOT NULL REFERENCES function_codes(function_code_id),
   base_power INT NOT NULL,
   move_type VARCHAR(20) NOT NULL REFERENCES pokemon_type(pokemon_type_id),
   damage_category MOVECLASS NOT NULL,
   accuracy NUMERIC(3, 2) NOT NULL,
   total_pp INT NOT NULL,
   effect_chance NUMERIC(3, 2) NOT NULL,
   move_priority INT NOT NULL,
   move_description VARCHAR(500) NOT NULL
);

CREATE TABLE pokemon_moves (
   pokemon_moves_id SERIAL PRIMARY KEY,
   pokemon_id VARCHAR(50) NOT NULL REFERENCES pokemon(pokemon_id),
   move_id VARCHAR(50) NOT NULL REFERENCES moves(move_id),
   learn_method VARCHAR(50) NOT NULL
);

CREATE TABLE technical_machines (
   technical_machine_id SERIAL PRIMARY KEY,
   game_item_id VARCHAR(30) NOT NULL REFERENCES game_items(game_item_id),
   move_id VARCHAR(50) NOT NULL REFERENCES moves(move_id)
);

CREATE TABLE flags (
   flag_id SERIAL PRIMARY KEY,
   flag_value CHAR(1) NOT NULL,
   flag_description VARCHAR(200) NOT NULL
);

CREATE TABLE move_flags (
   move_flag_id SERIAL PRIMARY KEY,
   move_id VARCHAR(50) NOT NULL REFERENCES moves(move_id),
   flag_id INT NOT NULL REFERENCES flags(flag_id)
);

CREATE TABLE egg_groups (
   egg_group_id VARCHAR(20) PRIMARY KEY
);

CREATE TABLE pokemon_egg_groups (
   pokemon_egg_group_id SERIAL PRIMARY KEY,
   pokemon_base_id INT NOT NULL REFERENCES pokemon_base(pokemon_base_id),
   egg_group_id VARCHAR(20) NOT NULL REFERENCES egg_groups(egg_group_id)
);

CREATE TABLE feedback (
   feedback_id SERIAL PRIMARY KEY,
   feedback_name VARCHAR(50) NOT NULL,
   feedback_content VARCHAR(2000)
);