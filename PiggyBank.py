print("Welcome to the Electronic Piggy Bank!\n")

#Collecting the initial value of the piggy bank
total = float(input("How much money is in the piggy bank so far? "))

#Setting variable 'i' for controlling when to break out of loop
i = 0

#Nested while loops
while i==0:
  #Menu listing options (formatted with tabs and spaces)
  print("\nMENU:\n\t(p) – Deposit a penny\n\t(n) – Deposit a nickel\n\t(d) – Deposit a dime\n\t(q) – Deposit a quarter\n\t(e) – Exit program and give balance\n")
  
  while True:
    #User input to select letter from menu
    letter = input("Please press a letter to select an option: ")

    #Control statements (if/elif/else)
    if letter == 'p':
      #Adding 1 cent to the intial value
      total+=0.01
      #Printing rounded value
      print(f"\nNew Balance: ${total:.2f}")
      continue

    elif letter == 'n':
      #Adding 5 cents to the intial value
      total+=0.05
      #Printing rounded value
      print(f"\nNew Balance: ${total:.2f}")
      continue
    
    elif letter == 'd':
      #Adding 10 cents to the intial value
      total+=0.1
      #Printing rounded value
      print(f"\nNew Balance: ${total:.2f}")
      continue
      
    elif letter == 'q':
      #Adding 25 cents to the intial value
      total+=0.25
      #Printing rounded value
      print(f"\nNew Balance: ${total:.2f}")
      continue
      
    elif letter == 'e':
      #Printing rounded value
      print(f"\nFinal Balance: ${total:.2f}")
      #Breaking out of first while loop to terminate program
      i+=1
      #Breaking out of this while loop
      break
      
    else:
      print("\nInvalid Option.")
      #Breaking out of loop to print the menu and wait for a new user input again
      break

#Final print statement, only printed after breaking out of the while loop
print("Goodbye")
