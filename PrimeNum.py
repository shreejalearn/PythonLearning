
print("Prime Number Checker\n")

num = int(input("Enter your number here: "))

if num > 1: 
   for i in range(2, num//2): 
    
       if (num % i) == 0: 
           print("\n", num, "is not a prime number") 
           break
   else: 
       print("\n",num, "is a prime number") 
  
else: 
   print("\nPlease enter a value above 1 (Anything below is neither prime nor composite).") 
