print("Number to Binary Converter\n")

user_input = input("Enter the number you'd like to convert into binary: \n")

user_num = int(user_input)

binary = bin(user_num)
int_binary = len(bin(user_num))

num = binary [2 : int_binary]

print(f"\nThe binary number of {user_num} is: "+ (num))
