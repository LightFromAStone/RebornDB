from bs4 import BeautifulSoup
import requests
import json

url = 'https://essentialsdocs.fandom.com/wiki/Function_codes'
response = requests.get(url, timeout=10)
content = BeautifulSoup(response.content, "html.parser")

all_codes = []

code_table = content.find_all('table', attrs={"class": "wikitable"})

for table in code_table:
   body = table.find('tbody')
   for row in body:
      code_obj = {
         "code": '',
         "effect": ''
      }

      th = row.find('th')
      td = row.find('td')

      if th != -1:
         text = th.get_text()
         if text.strip() != 'Function code':
            code_obj['code'] = text.strip()

      if td != -1:
         if td is not None:
            test = td.get_text().strip()
            test = test.replace('"', '\'')
            code_obj['effect'] = test
            all_codes.append(code_obj)
      
with open('scraper_function_codes.json', 'w') as outfile:
   json.dump(all_codes, outfile)

# out_file = open('output.txt', 'w')
# for code in all_codes:
#    out_file.write('Code: %s\n' % code.get('code'))
#    out_file.write('Effect: %s\n\n' % code.get('effect'))
# out_file.close()
   