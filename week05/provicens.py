def main():
  text_list = read_list("provinces.txt")
  print(text_list)

  #*Remove the first element of a list
  text_list.pop(0) #*pop() + the index 

  #*Remove the last element of a list 
  text_list.pop()

  #print(text_list)

  new_list = replace_str(text_list,"AB", "Alberta")

  #print(new_list)

  #print(f'\nAlberta occurs {count_number_elements(new_list, "Alberta")} in the modified list')

  print(f'\nAlberta occurs {new_list.count("Alberta")} in the modified list')

def read_list(filename):
  text_list = []

  with open(filename, "rt") as text_file:
    for row_line in text_file:
      # Remove white space, if there is any,
      # from the beginning and end of the line.
      clean_line = row_line.strip()
      text_list.append(clean_line)
  
  return text_list

def replace_str(list,ch,str): 
  for line in list:
    if ch in line:
      ch_index = list.index(ch)
      list[ch_index] = str
  return list

def count_number_elements(list,str): #You can use the build in function count()
  count = 0
  for line in list:
    if str in line:
      count += 1
  return count

if __name__ == '__main__':
  main()