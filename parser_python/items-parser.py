from asyncore import write


in_file = open('PBS/items.txt')
out_file = open('../sql_seeds/seed_items.sql', 'w')
tm_file = open('../sql_seeds/seed_TMs.sql', 'w')


lines =  in_file.readlines();
last = lines[-1]
in_file.seek(0,0)

out_file.write('INSERT INTO game_items (game_item_id, game_item_name, bag_pocket, game_item_price, game_item_description, in_battle_use_id, out_battle_use_id, special_items_use_id)\nVALUES\n')

tm_file.write('INSERT INTO technical_machines (game_item_id, move_id)\nVALUES\n')

# 1,REPEL,Repel,1,400,
# "An item that prevents any low-level wild Pokémon from jumping out at you for 100 steps."
# ,2,0,0, OPTIONAL 


#    game_item_id SERIAL PRIMARY KEY,
#    game_item_text_id VARCHAR(30) NOT NULL,
#    game_item_name VARCHAR(30) NOT NULL,
#    bag_pocket POCKET NOT NULL,
#    game_item_price INT NOT NULL,
#    game_item_description VARCHAR(200) NOT NULL,
#    in_battle_use_id INT NOT NULL REFERENCES in_battle_use(in_battle_use_id),
#    out_battle_use_id INT NOT NULL REFERENCES out_battle_use(out_battle_use_id),
#    special_items_use_id INT NOT NULL REFERENCES special_items_use(special_items_use_id)

# 0id - 1name id - 2name - 3pocket number - 4price - 5''

# description

# 0'' - 1out - 2in - 3special - 4optional 

pockets = ['', 'Items', 'Medicine', 'Poke Balls', 'TMs & HMs', 'Berries', 'Mail', 'Battle Items', 'Key Items']

# index = 0

for line in in_file:
   # index += 1
   line = line.rstrip()
   split_for_description = line.split('"')
   split_one = split_for_description[0].split(',')
   split_two = split_for_description[2].split(',')
   
   if(len(split_one[1]) > 30 or len(split_one[2]) > 30):
      print('FAILURE --- Item name is too long')
      break
   else:
      if split_one[2].count("'"):
         split_one[2] = split_one[2].replace("'", "''") 
      out_file.write(f"('{split_one[1]}', '{split_one[2]}', '{pockets[int(split_one[3])]}', {int(split_one[4])}, ")
   
   if (len(split_for_description[1]) > 200):
      print('FAILURE --- description is too long')
      break
   else:
      split_for_description[1] = split_for_description[1].replace("'", "''")
      out_file.write(f"'{split_for_description[1]}', {int(split_two[1]) + 1}, {int(split_two[2]) + 1}, {int(split_two[3]) + 1}")
   
   if(line == last):
      out_file.write(');')
   else:
      out_file.write('),\n')
      
   if (len(split_two) > 4 and split_two[4] != ""):
      tm_file.write(f"('{split_one[1]}', '{split_two[4]}'),\n")
   
   
in_file.close()
out_file.close()
tm_file.close()