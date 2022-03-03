in_file = open('PBS/tutor-moves.txt')
out_file = open('../sql_seeds/seed_pokemon_moves.sql', 'a')


current_move = ''
list_of_pokemon = []

for line in in_file:
   line = line.rstrip()
   line = line.lstrip()
   
   if '[' in line:
      current_move = line.replace('[', '').replace(']', '')
   elif ',' in line:
      list_of_pokemon = line.split(',')
      for pokemon in list_of_pokemon:
         out_file.write(f'("{pokemon}", "{current_move}", "TUTOR"),\n')

in_file.close()
in_file = open('PBS/tm.txt')

for line in in_file:
   line = line.rstrip()
   line = line.lstrip()

   if '[' in line:
      current_move = line.replace('[', '').replace(']', '')
   elif ',' in line:
      list_of_pokemon = line.split(',')
      for pokemon in list_of_pokemon:
         out_file.write(f'("{pokemon}", "{current_move}", "TM"),\n')


in_file.close()
in_file = open('../web_scrapers/alolan-move-data.txt')

method = ''
current_pokemon = ''

for line in in_file:
   line = line.rstrip()
   line = line.lstrip()
   if 'TM:' in line:
      method = 'TM'
   elif 'Tutoring:' in line:
      method = 'TUTOR'
   elif ',' in line:
      if method == 'TM' or method == 'TUTOR':
         list_of_moves = line.split(',')
         for move in list_of_moves:
            out_file.write(f'("{current_pokemon}", "{move}", "{method}"),\n')
         method = '' # reset method
   elif line.isupper():
      current_pokemon = line

in_file.close()
out_file.close()