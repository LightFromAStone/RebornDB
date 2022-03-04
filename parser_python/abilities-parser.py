#SCHEMA
#ID_number -> COMMA -> ID_text -> COMMA -> Name -> COMMA -> QUOTE -> Description -> QUOTE
# 1,STENCH,Stench,"Damaging a target makes it flinch by a small chance."


in_file = open('PBS/abilities.txt')
out_file = open('../sql_seeds/seed_abilities.sql', 'w')

out_file.write('INSERT INTO abilities (ability_id, ability_name, ability_description)\nVALUES\n')

# grab last line in file to use for comparisson later
lines =  in_file.readlines();
last = lines[-1]
in_file.seek(0,0)

for line in in_file:
   line = line.rstrip()
   split_values = line.split(',', 3) # only split to the 3rd comma
   split_values[3] = split_values[3].replace('"', '')
   split_values[3] = split_values[3][:-1] # this line removes the period at the end of each string
   if split_values[2].count("'"):
      split_values[2] = split_values[2].replace("'", "''")
   if split_values[3].count("'"):
      split_values[3] = split_values[3].replace("'", "''")
   out_file.write(f"('{split_values[1]}', '{split_values[2]}', '{split_values[3]}')")
   if line != last:
      out_file.write(',\n')
   else:
      out_file.write(';')
   
in_file.close()
out_file.close()