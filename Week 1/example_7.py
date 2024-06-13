# Example 7 elif 

# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))

# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount

# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")

#*Logical Operators (and, or, not)
driver = int(input("Driver What is your age? "))
passenger = int(input("passenger what is your age?"))
if driver >= 54 or (driver >= 32 and passenger >= 54):
    message = "Enjoy the ride!"

print(f"{message}")