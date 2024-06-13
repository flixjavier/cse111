def main():
  #create a list that contains five strings
  colors = ['Yellow', 'Red', 'Green', 'Yellow', 'Blue']

  #call the build in len function
  #print the length of the list
  length = len(colors)
  print(f'Number of elements: {length}')

  #print the element that is stored 
  #at index 2 in the colors list
  print(colors[2])

  #change the element that is stored at index 3 
  colors[3] = "Purple"

  #print the colors list
  print(colors)

#call main to start this program
if __name__ == "__main__":
  main()