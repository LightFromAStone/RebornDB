def gender_rate_to_float(rate):
   if rate == 'AlwaysMale':
      return 0.000
   elif rate == 'FemaleOneEighth':
      return 0.125
   elif rate == 'Female25Percent':
      return 0.250
   elif rate == 'Female50Percent':
      return 0.500
   elif rate == 'Female75Percent':
      return 0.750
   elif rate == 'FemaleSevenEighths':
      return 0.875
   elif rate == 'AlwaysFemale':
      return 1.000
   elif rate == 'Genderless':
      return -1.000


in_file = open('PBS/pokemon.txt')
out_base_pokemon = open('../sql_seeds/seed_base_pokemon.sql', 'w')
out_pokemon = open('../sql_seeds/seed_pokemon.sql', 'w')
out_wild_items = open('../sql_seeds/seed_wild_held_items.sql', 'w')
out_effort_points = open('../sql_seeds/seed_effort_points.sql', 'w')
out_base_stats = open('../sql_seeds/seed_base_stats.sql', 'w')
out_abilities_pokemon = open('../sql_seeds/seed_pokemon_abilities.sql', 'w')
out_evolutions = open('../sql_seeds/seed_evolutions.sql', 'w')
out_egg_groups_pokemon = open('../sql_seeds/seed_pokemon_egg_groups.sql', 'w')
out_moves_pokemon = open('../sql_seeds/seed_pokemon_moves.sql', 'w')


out_base_pokemon.write('INSERT INTO pokemon_base (pokemon_name, gender_rate, growth_type, catch_rate, hatch_steps)\nVALUES\n')

out_pokemon.write('INSERT INTO pokemon (pokemon_id, pokemon_base_id, pokemon_type_1, pokemon_type_2)\nVALUES\n')

out_wild_items.write('INSERT INTO wild_held_items (game_item_id, pokemon_id, held_chance)\nVALUES\n')

out_effort_points.write('INSERT INTO effort_points (pokemon_id, ev_hp, ev_attack, ev_defense, ev_speed, ev_sp_attack, ev_sp_defense)\nVALUES\n')

out_base_stats.write('INSERT INTO base_stats (pokemon_id, hp, attack, defense, speed, sp_attack, sp_defense)\nVALUES\n')

out_abilities_pokemon.write('INSERT INTO pokemon_abilities (pokemon_id, ability_id, is_hidden)\nVALUES\n')

out_evolutions.write('INSERT INTO evolutions (pokemon_id, evolves_into, evolution_method, evolution_method_param)\nVALUES\n')

out_egg_groups_pokemon.write('INSERT INTO pokemon_egg_groups (pokemon_base_id, egg_group_id)\nVALUES\n')

out_moves_pokemon.write('INSERT INTO pokemon_moves (pokemon_id, move_id, learn_method)\nVALUES\n')

# grab last line in file to use for comparisson later
lines =  in_file.readlines();
last = lines[-1]
in_file.seek(0,0)

final_pkmn = '807'
in_file.readline() #used to advance past the very first line
number_pkmn = '1'
id = ''
name = ''
type_1 = ''
type_2 = '' # need to reset
base_stats = ''
gender_rate = ''
growth_rate = ''
effort_points = ''
rareness = ''
abilities = ''
hidden_ability = ''
moves = ''
egg_moves = '' # need to reset
egg_groups = ''
hatch_steps = ''
wild_item_common = '' # need to reset
wild_item_uncommon = '' # need to reset
wild_item_rare = '' # need to reset
evolutions = ''

all_mons_array = []
all_types_array = ['NORMAL','FIRE','WATER','ELECTRIC','GRASS','ICE','FIGHTING','POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK','GHOST','DRAGON','DARK', 'STEEL', 'FAIRY']

for line in in_file:
   line = line.rstrip()
   line = line.lstrip()
   if line.count('InternalName='):
      id = line.replace('InternalName=', '')
      if id not in all_mons_array:
         all_mons_array.append(id)
      else:
         print(f'{id} has a duplicate')
      
   elif line.count('Name='):
      name = line.replace('Name=', '').replace("'", "''")
      
   elif line.count('Type1='):
      type_1 = line.replace('Type1=', '')
      if type_1 not in all_types_array:
         print(f'{type_1} is not in array')
      
   elif line.count('Type2='):
      type_2 = line.replace('Type2=', '')
      if type_2 not in all_types_array:
         print(f'{type_2} is not in array')
      
   elif line.count('BaseStats='):
      base_stats = line.replace('BaseStats=', '')
      
   elif line.count('GenderRate='):
      gender_rate = line.replace('GenderRate=', '')
      
   elif line.count('GrowthRate='):
      growth_rate = line.replace('GrowthRate=', '')
      
   elif line.count('EffortPoints='):
      effort_points = line.replace('EffortPoints=', '')
      
   elif line.count('Rareness='):
      rareness = line.replace('Rareness=', '')
      
   elif line.count('Abilities='):
      abilities = line.replace('Abilities=', '')
   
   elif line.count('HiddenAbility='):
      hidden_ability = line.replace('HiddenAbility=', '')
      
   elif line.count('EggMoves='):
      egg_moves = line.replace('EggMoves=', '')
      
   elif line.count('Moves='):
      moves = line.replace('Moves=', '')
      
   elif line.count('Compatibility='):
      egg_groups = line.replace('Compatibility=', '')
      
   elif line.count('StepsToHatch='):
      hatch_steps = line.replace('StepsToHatch=', '')
      
   elif line.count('Evolutions='):
      evolutions = line.replace('Evolutions=', '')
   
   elif line.count('WildItemCommon='):
      wild_item_common = line.replace('WildItemCommon=', '')
      
   elif line.count('WildItemUncommon='):
      wild_item_uncommon = line.replace('WildItemUncommon=', '')
      
   elif line.count('WildItemRare='):
      wild_item_rare = line.replace('WildItemRare=', '')
      
   elif line.count('[') and line.count(']'):
      end_chars = ''
      if number_pkmn == final_pkmn:
         end_chars = ';'
      else:
         end_chars = ',\n'
         
      # create entry in base_pokemon table if not an alolan form
      if not number_pkmn.count('A'):
         # check for alternate growth rate namings and convert them
         if growth_rate == 'Medium':
            growth_rate += ' Fast'
         elif growth_rate == 'Parabolic':
            growth_rate = 'Medium Slow'
         
         out_base_pokemon.write(f"('{name}', {gender_rate_to_float(gender_rate)}, '{growth_rate}', {rareness}, {hatch_steps}){end_chars}")
      
      # Create entry in pokemon table
      number_pkmn = number_pkmn.replace('[', '').replace(']', '').replace('A', '')
      out_pokemon.write(f"('{id}', {number_pkmn}, '{type_1}', ")
      if type_2 == '':
         out_pokemon.write(f'NULL){end_chars}')
      else:
         out_pokemon.write(f"'{type_2}'){end_chars}")
         type_2 = '' # reset type_2 in case next pokemon only has one type
      
      # Create entry in wild_held_items table if needed
      if wild_item_common or wild_item_uncommon or wild_item_rare:
         chance = 0.00
         item = item = wild_item_common
         if wild_item_common == wild_item_uncommon and wild_item_uncommon == wild_item_rare:
            chance = 1.00
         elif wild_item_common != '':
            chance = 0.50
         elif wild_item_uncommon != '':
            chance = 0.05
            item = wild_item_uncommon
         else:
            chance = 0.01
            item = wild_item_rare
         out_wild_items.write(f"('{item}', '{id}', {chance}),\n")
         # reset wild item variables
         wild_item_common = ''
         wild_item_uncommon = ''
         wild_item_rare = ''
      
      # Create entry for effort_points table
      points = effort_points.split(',')
      out_effort_points.write(f"('{id}', {points[0]}, {points[1]}, {points[2]}, {points[3]}, {points[4]}, {points[5]}){end_chars}")
      
      # Create entry in base_stats table
      stats = base_stats.split(',')
      out_base_stats.write(f"('{id}', {stats[0]}, {stats[1]}, {stats[2]}, {stats[3]}, {stats[4]}, {stats[5]}){end_chars}")
      
      # Create entries for pokemon_abilities table
      if hidden_ability:
         out_abilities_pokemon.write(f"('{id}', '{hidden_ability}', TRUE),\n")
         hidden_ability = '' # reset in case next pokemon has no hidden ability
      ability = abilities.split(',')
      for a in ability:
         out_abilities_pokemon.write(f"('{id}', '{a}', FALSE)")
         if number_pkmn == final_pkmn and a == ability[-1]:
            out_abilities_pokemon.write(';')
         else:
            out_abilities_pokemon.write(',\n')
      
      # Create entries in evolutions table
      if evolutions:
         data = evolutions.split(',')
         data_length = len(data)
         count =  0
         while count < data_length:
            out_evolutions.write(f"('{id}', '{data[count]}', '{data[count + 1]}', ")
            if data[count + 2]:
               out_evolutions.write(f"'{data[count + 2]}')")
            else:
               out_evolutions.write('NULL)')
            count += 3
            if count < data_length:
               out_evolutions.write(',\n')
            elif number_pkmn == '803':
               out_evolutions.write(';')
            else:
               out_evolutions.write(',\n')
      
      # Create entries in pokemon_egg_groups
      group = egg_groups.split(',')
      out_egg_groups_pokemon.write(f"({number_pkmn}, '{group[0]}'){end_chars}")
      if len(group) == 2:
         out_egg_groups_pokemon.write(f"({number_pkmn}, '{group[1]}'){end_chars}")
         
      # Create entries in pokemon_moves table
      move_data = moves.split(',')
      move_data_length = len(move_data)
      count = 0
      while count < move_data_length:
         out_moves_pokemon.write(f"('{id}', '{move_data[count + 1]}', '{move_data[count]}'),\n")
         count += 2
      
      egg_data = egg_moves.split(',')
      for move in egg_data:
         out_moves_pokemon.write(f"('{id}', '{move}', 'EGG'),\n")
            
                     
      number_pkmn = line.replace('[', '').replace(']', '')
         
      
out_mons = open('all-pkmn.txt', 'w')   
out_mons.write(f'{all_mons_array}')
 
 
 
 
 
   
in_file.close()
out_base_pokemon.close()
out_pokemon.close()
out_wild_items.close()
out_effort_points.close()
out_base_stats.close()
out_abilities_pokemon.close()
out_evolutions.close()
out_egg_groups_pokemon.close()
out_moves_pokemon.close()