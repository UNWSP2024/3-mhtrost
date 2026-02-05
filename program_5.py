# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 


HOT_DOG_PRICE = 3.50
CHILI_DOG_PRICE = 4.50
CHEESE_PRICE = 0.50
PEPPERS_PRICE = 0.75
ONIONS_PRICE = 1.00
TAX_RATE = 0.07

print("Hot Dog Menu:")
print("1. Hot Dog ($3.50)")
print("2. Chili Dog ($4.50)")

choice = input("Enter the number of the hot dog you want: ")

if choice == "1":
    subtotal = HOT_DOG_PRICE
elif choice == "2":
    subtotal = CHILI_DOG_PRICE
else:
    print("Invalid choice.")
    exit()

cheese = input("Add cheese for $0.50? (y/n): ")
peppers = input("Add peppers for $0.75? (y/n): ")
onions = input("Add grilled onions for $1.00? (y/n): ")

if cheese == "y":
    subtotal += CHEESE_PRICE
if peppers == "y":
    subtotal += PEPPERS_PRICE
if onions == "y":
    subtotal += ONIONS_PRICE

tax = subtotal * TAX_RATE
total = subtotal + tax

print("Order Summary")
print(f"Hot dog cost: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total cost: ${total:.2f}")
