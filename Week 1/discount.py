from datetime import datetime

""" Problem Statement
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
 """
#TODO
#* write a program discount.py
#* Gets a customer subtotal as Input
#* Get the current day of the week
#* Calculates the total cost after applying
#* get the day from your system 
#TODO Core Requirements
#* Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer’s operating system.
#* Your program correctly computes and prints the discount amount if applicable.
#* Your program correctly computes and prints the sales tax amount and the total amount due.

#Calculate Discount Amount variables
salesTaxPercentage = 0.06
discountTax = 0.1
salesDiscount = 0 
totalDue = 0
discountTotal = 0
amountToDiscount = 0
customerSubTotal = 0

#Get customer subtotal
price = 1
while price != 0:
    # Get the price from the user.
    price = float(input("Please enter the price: $ "))
    if price != 0:
        # Get the quantity from the user.
        quantity = int(input("Please enter the quantity: "))
        customerSubTotal += price * quantity

        # Print a blank line.
        print()

#Get Day of Week
currentDateTime = datetime.now()

currentDay = currentDateTime.weekday()


#check if it's Tuesday or Wednesday
if (currentDay == 2 or currentDay == 3) and (customerSubTotal >= 50):
  salesDiscount = customerSubTotal * discountTax
  discountTotal = customerSubTotal - salesDiscount
  salesTax = discountTotal * salesTaxPercentage
  totalDue = discountTotal + salesTax
  print(f'The 10% discount amount: ${salesDiscount:.2f}')
  print(f'Sales  Tax: ${salesTax:.2f}')
  print(f'Total: ${totalDue:.2f}')
elif (currentDay == 1 or currentDay == 2) and (customerSubTotal < 50):
  #If not enough for a full discount
  amountToDiscount = 50 - customerSubTotal
  print(f'You need ${amountToDiscount} to get a full 10% discount.')
  salesTax = customerSubTotal * salesTaxPercentage
  totalDue = customerSubTotal + salesTax
  print(f'Sales  Tax: ${salesTax:.2f}')
  print(f'Total: ${totalDue:.2f}')

#Rest of the days
else:
  salesTax = customerSubTotal *  salesTaxPercentage
  totalDue = customerSubTotal + salesTax
  print(f'Sales  Tax: ${salesTax:.2f}')
  print(f'Total: ${totalDue:.2f}')

