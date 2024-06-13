import csv
import random
import string
from datetime import datetime

STORE_NAME = "Inkom Emporium"
STORE_MESSAGE = "Thank you for shopping at the"
PRODUCTS_DATA = "products.csv"
REQUEST_DATA = "request.csv"
KEY_COLUMN_INDEX = 0
PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
PRODUCT_QUANTITY_INDEX = 1
SALES_TAX = 0.06
DISCOUND_TAX = 0.1
SURVEY_WEB_SITE = 'https://www.surveymonkey.com/'

def main():
  try:
    #Get the current datetime
    currentDateTime = datetime.now()
    currentDay = currentDateTime.weekday()

    products_dict = read_dictionary(PRODUCTS_DATA, KEY_COLUMN_INDEX)
    #print(products_dict)

    print(f"{STORE_NAME}\n")
    request_list = []

    with open(REQUEST_DATA, 'rt') as csv_request:
      reader = csv.reader(csv_request)
      next(reader)

      for line in reader:
        if len(line) !=0:
          request_list.append(line)
    # end open file
    
    #for loop 
    ordered_times = 0
    subtotal = 0

    for product in request_list:
      product_value = products_dict[product[PRODUCT_ID_INDEX]]
      product_name = product_value[PRODUCT_NAME_INDEX]
      product_price = product_value[PRODUCT_PRICE_INDEX]

      print(f'{product_name}: {product[PRODUCT_QUANTITY_INDEX]} @ {product_price}')

      subtotal += float(product[PRODUCT_QUANTITY_INDEX]) * float(product_price)

      #count the number of items
      ordered_times += int(product[PRODUCT_QUANTITY_INDEX])
      
    # print number of items
    print(f"\nNumber of Items: {ordered_times}")

    #check if it's Tuesday or Wednesday
    if (currentDay == 2 or currentDay == 3):
      salesDiscount = subtotal * DISCOUND_TAX
      discountTotal = subtotal - salesDiscount
      salesTax = discountTotal * SALES_TAX
      total_amount = discountTotal + salesTax
      print(f'The 10% discount amount: ${salesDiscount:.2f}')
      print(f'Sales  Tax: ${salesTax:.2f}')
      print(f'Total: ${total_amount:.2f}')
    
    else:
      #add subtotal
      print(f'Subtotal: {subtotal:.2f}')

      #Sales Tax
      sales_tax = subtotal * SALES_TAX
      print(f'Sales Tax: {sales_tax:.2f}')

      #Total
      total_amount = subtotal + sales_tax
      print(f'Total: {total_amount:.2f}\n')

    print(free_coupon(random_product(request_list, products_dict)))

    print(f'\n{STORE_MESSAGE} {STORE_NAME}.\n{currentDateTime:%a %b %d %H:%M:%S %Y}')

    print(online_survey(SURVEY_WEB_SITE))
  
  except FileNotFoundError as no_file_err:
    print('Data not Found: Something went wrong, No Data File found')

  except PermissionError as no_permission_err:
    print("Permission denied: You don't have the necessary permissions to change the permissions of this file.")

  except KeyError as no_key_error: 
    print('Key Error: unknown product ID in the request.csv file')


def read_dictionary(filename, key_colum_index): 
  dictionay = {}

  with open(filename, 'rt') as csv_file:
    # Comment: 
    reader = csv.reader(csv_file)

    next(reader)

    for row_line in reader: 
      if len(row_line) != 0:
        key = row_line[key_colum_index]
        dictionay[key] = row_line
  # end open file
  return dictionay

def online_survey(survey):
  return (f"\nYour opinion is important to us. Please answer the following survey\n{survey}\nThank You!")

def free_coupon(product):
  coupon_code = generate_coupon_code()
  return (f"Thank you for purchasing {product}.\nHere is a 10% discount on your next purchase.\nYour coupon code is: {coupon_code}")

def generate_coupon_code(length=10):
    #I ask Chat GTP help with this function
    characters = string.ascii_uppercase + string.digits
    coupon_code = ''.join(random.choice(characters) for _ in range(length))
    return coupon_code

def random_product(list,dictionary):
  #Create a coupon for a random product. 
    #from the list of products (request list) i will select a random product and create a coupon
    #First chose a random product from the request list
    #create a variable just with the ID of the product
    #Using that ID as Key, extract the info from the products dictionary
    #From that variable extract just the name of the product. 
    random_product = random.choice(list)
    random_product_ID = random_product[PRODUCT_ID_INDEX]

    random_product_value = dictionary[random_product_ID]

    random_product_name = random_product_value[PRODUCT_NAME_INDEX]

    return random_product_name


if __name__ == "__main__":
  main()