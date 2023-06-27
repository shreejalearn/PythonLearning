print("PostFix Calculator")

#Sets up user's first input number (this is the value that gets printed at the end since the other user inputs are added/subtracted/multiplied/divided from this value)
main_1 = 0

#Sets up user's input beyond their first input...this is the temporary storage variable until the user's input gets added/subtracted/multiplied/divided from the first input (input_1). This is named num_end since it only supports either the float values the user inputs or an equal sign to end the program.
num_end = 0

#Sets up an empty string for collecting the user inputs on the operators that's going to be used
operator=""

#Boolean value determining if this is the user's first input or not
first_input = True

while True:
  #Only runs for the user's first input
  if first_input == True:
    #Expects a float value since standard postfix form is num, num, op...(this is programmed to raise a ValueError if user tries to enter anything other than a float or tries to enter a operator instead)
    main_1 = float(input())
    
  #Collects user's next input (expected to be a number or equal sign)
  num_end = input()
  #If user's input is an equal sign here...the user entered something like [3 =] and the program is going to raise a Syntax Error or the user entered something like [4 3 + =] which will print [7.00] the user's formatted calculation
  if num_end == "=":
    #Makes sure user isn't able to enter an equal sign after the first number...something like [3=]
    if first_input==True:
      raise SyntaxError("Read token %s, expected number" % num_end)
    #Breaks out of loop upon entering equal sign
    else:
      break
  #Ensures the first loop doesn't run again
  first_input=False
  #If user's input is not an equal sign, it is expected to be a number...if it's not a number either, then the program will automatically raise a ValueError for not following standard Postfix form
  num_end = float(num_end)
  #Input used for collecting the operators entered
  operator = input()

  #Control statements to control the flow of the program and carry out the calculation based on the entries above
  if(operator == "+"):
    #Adding the new input(s) to the total
    main_1 += num_end
  elif(operator == "-"):
     #Subtracted the new input(s) from the total
    main_1 -= num_end
  elif(operator == "*"):
    #Multiplied the new input(s) to the total
    main_1 *= num_end
  elif(operator == "/"):
    #Divided the new input(s) from the total
    main_1 /= num_end
    
  #Supports raising a number to the power as well
  elif operator=="^":
    #Raises the first number to the power of the second number
    main_1**=num_end

  #Only runs if the user tries to enter a number or invalid/unsupported characters in the input collecting the operator
  else:
    raise SyntaxError("Read token %s, expected operator" % operator)

#Formats and prints the main_1...which contains the looped through and edited version of the first number based on the number of calculations performed by users
print(f"\n{main_1:.2f}")
