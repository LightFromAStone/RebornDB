#  ----------- Begin code for creating moves-array.txt -----------


# in_file = open('PBS/moves.txt')
# out_file = open('../sql_seeds/moves-array.txt', 'w')

# out_file.write('movesArray = [')

# lines =  in_file.readlines();
# last = lines[-1]
# in_file.seek(0,0)

# for line in in_file:
#    line = line.rstrip()
#    split_values = line.split(',', 3) # only split to the 3rd comma
#    out_file.write(f'"{split_values[1]}", "{split_values[2]}"')
#    if line != last:
#       out_file.write(', ')
#    else:
#       out_file.write('];')


#  ----------- End code for moves-array.txt -----------


# 1,MEGAHORN,Megahorn,000,120,BUG,Physical,85,10,0,00,0,abef,"Using a tough and impressive horn, the user rams into the target with no letup."

def convert_to_float_string(str):
   if str == '100':
      return '1.00, '
   elif str == '0':
      return '0.00, '
   else:
      return f'0.{str}, '

in_file = open('PBS/moves.txt')
out_file = open('../sql_seeds/seed_moves.sql', 'w')
out_move_flags = open('../sql_seeds/seed_move_flags.sql', 'w')

out_file.write('INSERT INTO moves (move_id, move_name, function_code_id, base_power, move_type, damage_category, accuracy, total_pp, effect_chance, move_priority, move_description)\nVALUES\n')

out_move_flags.write('INSERT INTO move_flags (move_id, flag_id)\nVALUES\n')

lines =  in_file.readlines();
last = lines[-1]
in_file.seek(0,0)

for line in in_file:
   line = line.rstrip()
   split_values = line.split(',', 13) # only split to the 13th comma (prevents splitting description that has commas)
   out_file.write(f'("{split_values[1]}", "{split_values[2]}", "{split_values[3]}", {split_values[4]}, "{split_values[5]}", "{split_values[6]}", ')
   
   # write values as decimal for accuracy
   out_file.write(convert_to_float_string(split_values[7]))
      
   out_file.write(f'{split_values[8]}, ')
   
   # write values as decimal for effect_chance
   out_file.write(convert_to_float_string(split_values[9]))
   
   # skip split_values[10], unused. Represents moves target
   
   out_file.write(f'{split_values[11]}, ')
   
   if len(split_values[13]) > 500:
      print(f'ERROR! ---- Descripiton greater than 500\n{split_values[13]}')
   out_file.write(f'{split_values[13]})')
      
   if line != last:
      out_file.write(',\n')
   else:
      out_file.write(';')
      
   # Handle move_flags (split_values[12])
   if split_values[12] != '':
      # flags = split_values[12].split('')
      for flag in split_values[12]:
         out_move_flags.write(f'("{split_values[1]}", {ord(flag) - 96})')
         # this if/else only works because I know the last item in the moves.text file has flags
         if line == last and flag == split_values[12][-1]:
            out_move_flags.write(';')
         else:
            out_move_flags.write(',\n')
   
   
   
   
   
in_file.close()
out_file.close()
out_move_flags.close()