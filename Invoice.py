names = [] # The list of item names
counts = [] # The list of item counts
prices = [] # The list of item prices

print("This program will help to calculate the customer's invoice.\n")

#The name of the first item purchased
name = input("Please enter the name of the first item purchased. ")
#Storing the string version of the input to the list names
names.append(str(name))

#The amount of the first item purchased
num_of_items = input("How many were purchased? ")
#Storing the integer version of the input to the list counts
counts.append(int(num_of_items))

#The price of the first item purchased
price = input("What was the price for each one? ")
#Storing the decimal version of the input to the list prices
prices.append(float(price))

print("\n") #new line

#exit is only True when user hits enter instead of typing in the name of a purchase
exit=False

while exit==False:
  #The name of the items purchased
  name = input ("Please enter the name of the item purchased. ")
  
  if name=="":
      #Loops the input as many times as the user wants until the user presses enter
    exit=True
    #breaks out of loop
    
  else:
    #if user enters an item to purchase it adds it to the list names
    names.append(str(name))
    
    #The amount of the item purchased
    num_of_items = input("How many were purchased? ")
    #adds the number of items to the list counts
    counts.append(int(num_of_items))
    
    #The price of the item purchased
    price = input("What was the price for each one? ")
    #adds the price of the items to the list prices
    prices.append(float(price))
  
    print("\nName of the next item purchased. Press enter when you are done.")
    #continues the loop


print("\nHere's your invoice: \n")
print(f"{'Items':<10s}{'Count':>10s}{'Item Price':>15s}{'Item Total':>15s}")

#Setting a counter for the index of the list
i=0
#Setting the sum of total prices to 0
sum=0

#Looping for the length of number of items purchased/added in the list
for i in range(len(names)):
  #i is the index, starting at 0 and 1 is added each time the loop runs
  print(f"{names[i]:<10s}{counts[i]:>10d}{prices[i]:>15.2f}{(float(prices[i])*int(counts[i])):>15.2f}")
  #prices[i]*counts[i] multiplies the unit price by the amount of the item purchased
  sum+=prices[i]*counts[i] #adds to the sum variable
  #increments the index by 1 each time the loop runs
  i+=1

print(f"\nGrand Total: ${sum:.2f}")
