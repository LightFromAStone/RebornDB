in_file = open('PBS/moves.txt')
out_file = open('../sql_seeds/moves-array.txt', 'w')

out_file.write('movesArray = [')

lines =  in_file.readlines();
last = lines[-1]
in_file.seek(0,0)

for line in in_file:
   line = line.rstrip()
   split_values = line.split(',', 3) # only split to the 3rd comma
   out_file.write(f'"{split_values[1]}", "{split_values[2]}"')
   if line != last:
      out_file.write(', ')
   else:
      out_file.write('];')