print("This program will help to calculate the customer's invoice.")

#Collecting user information for first item
#Item stored as string
item = input("\nPlease enter the name of the first item purchased: ")
#Quantity stored as integer
quantity = int(input("How many were purchased? "))
#Price stored as float
price = float(input("What was the price for each one? "))

#Collecting user information for second item
#Item stored as string
item2 = input("\nPlease enter the name of the second item purchased: ")
#Quantity stored as integer
quantity2 = int(input("How many were purchased? "))
#Price stored as float
price2 = float(input("What was the price for each one? "))

#Printing for item 1
print("\n\nItem 1:")
#String formatted to round integers
print(f"\t{str(quantity)} {item} ${price:.2f} each")
print(f"\tTotal cost: ${(price*quantity):.2f}")

#Printing for item 2
print("\n\nItem 2:")
#String formatted to round integers
print(f"\t{str(quantity2)} {item2} ${price2:.2f} each")
print(f"\tTotal cost: ${(price2*quantity2):.2f}")

#Storing grand total price in variable
total = (price * quantity) + (price2 * quantity2)

print(f"\nGrand total: {total:.2f}")
