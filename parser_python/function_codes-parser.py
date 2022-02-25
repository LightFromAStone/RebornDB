import json

file = open('../web_scrapers/scraper_function_codes.json')

data = json.load(file)

output_file = open('../sql_seeds/seed_function_codes.sql', 'w')

output_file.write('INSERT INTO function_codes (function_code_value, function_code_description)\nVALUES\n')

for code in data:
   c = code.get('code')
   d = code.get('effect')
   d = d.replace('\n', '\\n')
   output_file.write(f'("{c}", "{d}")')
   if code == data[-1]:
      output_file.write(';')
   else:
      output_file.write(',\n')