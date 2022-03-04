import json

file = open('../web_scrapers/scraper_function_codes.json')

data = json.load(file)

output_file = open('../sql_seeds/seed_function_codes.sql', 'w')

output_file.write('INSERT INTO function_codes (function_code_id, function_code_description)\nVALUES\n')

out_code_array = open('../sql_seeds/function_code_array.txt', 'w')
out_code_array.write('code_array = [')

for code in data:
   c = code.get('code')
   out_code_array.write(f'"{c}", ')
   d = code.get('effect')
   d = d.replace('\n', '\\n')
   d = d.replace("'", "''")
   output_file.write(f"('{c}', '{d}')")
   if code == data[-1]:
      # including special codes not in json file
      output_file.write(",\n('176', 'Deals damage. If the user''s Attack stat is higher than its Special Attack stat, move becomes a physical move; otherwise (i.e. if the user''s Special Attack is greater than or equal to its Attack) it is a special move. During the execution of the move, all ignorable Abilities that could affect the success or damage of a move are ignored, except when this move is called by another move rather than directly used.\\nFor determining which stat is higher, stat stage-modifiers are taken into account, but other effects (e.g. held items such as a Choice Band, Abilities such as Huge Power, burn, etc.) are not.'),\n")
      
      output_file.write("('177', 'Inflicts damage. In the remainder of the current turn, all Normal-type moves will become Electric-type, including status moves.\\nThe type-changing effect is applied after move type-changing Abilities, so cannot affect an originally Normal-type move used by a Pokémon with Pixilate but can affect an originally Fairy-type move used by a Pokémon with Normalize.')")
      output_file.write(';')
   else:
      output_file.write(',\n')