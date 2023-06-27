input("Please enter the following values as directed and type 'e' when you would like to exit the program. Press enter to continue.")

def factorial(n):
    if n == 0:
        return 1
    else:
      return n * factorial(n-1)
        
a = "0"
b = int(a)

while b >= 0:
    a = input("\nEnter a number: ")
    if a[0] == "e":
        break
    b = int(a)
    print("\n" + str(b) +"! is " + str(factorial(b)))

print("\nThank you for using this tool!! Click 'run again' to restart this calculator!")
