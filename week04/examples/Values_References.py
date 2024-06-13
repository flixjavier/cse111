def main():
  #example 10
  #x = 17
  #y = x #copies the value of some data types (boolean, integer, float) 
  #print(f"Before changing x: x {x}  y {y}")
  #x += 1
  #print(f"After changing x:  x {x}  y {y}")
  ## Example 11 python works different between integers and list. 

  #lx = [7, -2]
  #copies the reference for other data types (list and other large data types) 
  #ly = lx #your are not creating a new variable, you a re creating a reference to the lx list. 
  #print(f"Before changing lx: lx {lx}  ly {ly}")
  #lx.append(5)
  #print(f"After changing lx:  lx {lx}  ly {ly}")

  #**Pass by Value and Pass by Reference
  #Example11

  print("main()")
  x = 5
  lx = [7, -2]
  print(f"Before calling modify_args(): x {x}  lx {lx}")

  # Pass one integer and one list
  # to the modify_args function.
  modify_args(x, lx)

  print(f"After calling modify_args():  x {x}  lx {lx}")

def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1 #pass vy value
    alist.append(4) #Pass vy reference

    print(f"   After changing n and alist:  n {n}  alist {alist}")

# Call main to start this program.
if __name__ == "__main__":
  main()