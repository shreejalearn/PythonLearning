print("Exponential Calculator \n"
)

print("Please enter the range of numbers you would like to raise to an exponential power: \n")

try:
  value_1 = int(input("Number(Required): "))

  input_value = input("Number(Optional): ")
  if (input_value == ""):
    value_2 = value_1
  else:
    value_2 = int(input_value)

  if value_1 > value_2:
    value_2 = value_1
    value_1 = int(input_value)

  print("\nThanks! What exponent would you like to raise these numbers to? \n")

  exponent = int(input("Exponent(Required): "))

  for i in range (value_1, value_2 + 1):
    print("No. {0:2} when raised to the power of {1:3} is {2:3}".format(i, exponent, i**exponent))

except:
  print("\nError. Make sure that all values entered as integers and that all required values are filled in!")
