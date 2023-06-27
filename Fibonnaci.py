# 0, 1, 1, 2, 3, 5, 8, 13, 21... Fibonnaci Numbers

our_input = int(input("How many series of numbers? "))

prev_num = 0
next_num = 1

increase_by = 0


if our_input <= 0:
  print("\nError. Please enter a value above 0.")

elif our_input == 1:
  
   print("\nFibonacci series for", our_input,": ")
   print(prev_num)

else:
   print("\nFibonacci series until", our_input, ":\n")

   while increase_by <= our_input:
    print(prev_num)

    add = prev_num + next_num

    prev_num = next_num
    next_num = add

    increase_by += 1

