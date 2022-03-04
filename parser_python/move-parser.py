code_array = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "009", "00A", "00B", "00C", "00D", "00E", "00F", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "01A", "01B", "01C", "01D", "01E", "01F", "020", "021", "022", "023", "024", "025", "026", "027", "028", "029", "02A", "02B", "02C", "02D", "02E", "02F", "030", "031", "032", "033", "034", "035", "036", "037", "038", "039", "03A", "03B", "03C", "03D", "03E", "03F", "040", "041", "042", "043", "044", "045", "046", "047", "048", "049", "04A", "04B", "04C", "04D", "04E", "04F", "050", "051", "052", "053", "054", "055", "056", "057", "058", "059", "05A", "05B", "05C", "05D", "05E", "05F", "060", "061", "062", "063", "064", "065", "066", "067", "068", "069", "06A", "06B", "06C", "06D", "06E", "06F", "070", "071", "072", "073", "074", "075", "076", "077", "078", "079", "07A", "07B", "07C", "07D", "07E", "07F", "080", "081", "082", "083", "084", "085", "086", "087", "088", "089", "08A", "08B", "08C", "08D", "08E", "08F", "090", "091", "092", "093", "094", "095", "096", "097", "098", "099", "09A", "09B", "09C", "09D", "09E", "09F", "0A0", "0A1", "0A2", "0A3", "0A4", "0A5", "0A6", "0A7", "0A8", "0A9", "0AA", "0AB", "0AC", "0AD", "0AE", "0AF", "0B0", "0B1", "0B2", "0B3", "0B4", "0B5", "0B6", "0B7", "0B8", "0B9", "0BA", "0BB", "0BC", "0BD", "0BE", "0BF", "0C0", "0C1", "0C2", "0C3", "0C4", "0C5", "0C6", "0C7", "0C8", "0C9", "0CA", "0CB", "0CC", "0CD", "0CE", "0CF", "0D0", "0D1", "0D2", "0D3", "0D4", "0D5", "0D6", "0D7", "0D8", "0D9", "0DA", "0DB", "0DC", "0DD", "0DE", "0DF", "0E0", "0E1", "0E2", "0E3", "0E4", "0E5", "0E6", "0E7", "0E8", "0E9", "0EA", "0EB", "0EC", "0ED", "0EE", "0EF", "0F0", "0F1", "0F2", "0F3", "0F4", "0F5", "0F6", "0F7", "0F8", "0F9", "0FA", "0FB", "0FC", "0FD", "0FE", "0FF", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "10A", "10B", "10C", "10D", "10E", "10F", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "11A", "11B", "11C", "11D", "11E", "11F", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "12A", "12B", "12C", "12D", "12E", "12F", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "13A", "13B", "13C", "13D", "13E", "13F", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "14A", "14B", "14C", "14D", "14E", "14F", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "15A", "15B", "15C", "15D", "15E", "15F", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "16A", "16B", "16C", "16D", "16E", "16F", "170", "171", "172", "173", "174", "175"]
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

all_moves = []

lines =  in_file.readlines();
last = lines[-1]
in_file.seek(0,0)

for line in in_file:
   line = line.rstrip()
   line = line.lstrip()
   split_values = line.split(',', 13) # only split to the 13th comma (prevents splitting description that has commas)
   if split_values[1] not in all_moves:
      all_moves.append(split_values[1])
   else:
      print(f'{split_values[1]} already exists')
   count = 0
   while count < len(split_values):
      split_values[count] = split_values[count].replace("'", "''")
      count += 1
   split_values[3] = split_values[3].lstrip()
   if len(split_values[3]) > 3 or len(split_values[3]) < 3:
      print(f'function code of {split_values[1]} is not correct')
   if split_values[3] not in code_array:
      print(f'{split_values[3]} is not listed in the array. Item {split_values[1]}')
   out_file.write(f"('{split_values[1]}', '{split_values[2]}', '{split_values[3]}', {split_values[4]}, '{split_values[5]}', '{split_values[6]}', ")
   
   # write values as decimal for accuracy
   out_file.write(convert_to_float_string(split_values[7]))
      
   out_file.write(f'{split_values[8]}, ')
   
   # write values as decimal for effect_chance
   out_file.write(convert_to_float_string(split_values[9]))
   
   # skip split_values[10], unused. Represents moves target
   
   out_file.write(f'{split_values[11]}, ')
   
   if len(split_values[13]) > 500:
      print(f'ERROR! ---- Descripiton greater than 500\n{split_values[13]}')
   split_values[13] = split_values[13].replace('"', '')
   out_file.write(f"'{split_values[13]}')")
      
   if line != last:
      out_file.write(',\n')
   else:
      out_file.write(';')
      
   # Handle move_flags (split_values[12])
   if split_values[12] != '':
      # flags = split_values[12].split('')
      for flag in split_values[12]:
         out_move_flags.write(f"('{split_values[1]}', {ord(flag) - 96})")
         # this if/else only works because I know the last item in the moves.text file has flags
         if line == last and flag == split_values[12][-1]:
            out_move_flags.write(';')
         else:
            out_move_flags.write(',\n')
   
   
   
   
   
in_file.close()
out_file.close()
out_move_flags.close()