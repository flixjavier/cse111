#Example 2

def main():
  #create an empty list will hold fabric names
  fabrics = []
  
  #add three elements at the end of the list
  fabrics.append("velvet")
  fabrics.append("denim")
  fabrics.append("gingham")

  #insert an element at the beggining of the list
  fabrics.insert(0,"Chiffon")
  print (fabrics)

  #Determine if gingham is in the list
  if "gingham" in fabrics:
    print("is in the list")
  else:
    print('No is not')

  # Get the index where velvet is stored in the fabrics list.
  index = fabrics.index("velvet")

  #replace velvet with taffeta

  fabrics[index] = 'taffeta'

  #Remove the last element of the list
  fabrics.pop()

  #remove deni from the list
  fabrics.remove('denim')

  #get the length of the list

  n = len(fabrics)
  print (f'The number of elements in the list: {n}')
  print(fabrics)

#call main 
if __name__ == '__main__':
  main()

  
