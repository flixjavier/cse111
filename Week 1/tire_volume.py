import math
from datetime import datetime
#Prove that you can write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see.

""" 
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches. """

#TODO
#*Gets the current date from the computer’s operating system.
#*Opens a text file named volumes.txt for appending.
#*Appends to the end of the volumes.txt file one line of text that contains the following five values:
""" current date, width of the tire, aspect ratio of the tire, diameter of the wheel, volume of the tire"""

#function to calculate the volume of a tire
def calculateVolumeTire (width, aspect , diameter):
  denominator = 10000000000
  volumeOfTire = (constantPI * (pow(width,2)) * aspect * ((width * aspect) + (2540 * diameter))) / denominator
  return volumeOfTire

#variables: size of a car tire
widthInMM = float(input('Enter the width of the tire in mm (ex 205): '))
aspectRatio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameterInInches = float(input('Enter the diameter of the wheel in inches (ex 15): '))
userPhone = ''
userFirstName = ''
userLastName = ''
userPhone = ''
constantPI = math.pi 

#Get Current date

currentDate = datetime.now()

#get the Volume of Tire
volumeTire = calculateVolumeTire(widthInMM, aspectRatio, diameterInInches)

#Open a text file named volume.txt and append data to file. 
def appendTireInfo():
  with open('volumes.txt', 'at') as volumes_tire:
    volumes_tire.write(f'{currentDate:%Y-%m-%d}, {int(widthInMM)}, {int(aspectRatio)}, {int(diameterInInches)}, {volumeTire:.2f}  {userLastName} {userFirstName} {userPhone}\n\n')

#result
print(f'\nThe approximate volume is {(volumeTire):.2f} liters')

#Ask the user if he wants to buy 

userBuy = input(f'Would you like to buy that tire with this dimension {volumeTire:.2f} liters? (y/n): ')

if (userBuy == 'y') or (userBuy == 'yes'):
  userPhone = input('What is your phone number? ')
  userLastName = input('What is your last name? ')
  userFirstName = input('What is your first name? ')
  appendTireInfo()
  print('\nYour order has been placed! Thank You!\n')
else:
  print("\nOkay, thank you so much for considering our store.")
  appendTireInfo()

