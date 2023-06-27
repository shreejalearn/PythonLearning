#print statements to introduce program
print("This program will calculate simple and compound interest for you.")
print("Simply enter the parameter values!")

#takes user input for principal amount
principal = float(input("What is the starting amount (principal) of your deposit? "))

#takes user input for annual interest rate
interest_rate = float(input("What is the annual interest rate (%) of the account? "))

#takes user input for the amount of years they'll leave the money in account
len_year = float(input("For how many years will you leave the money in the account? "))

#takes user input for the number of times the account compounds
num_deposits = int(input("How many times does the account compound per year? "))

#calculating simple interest using formula
simple_interest = round(principal + (principal*(interest_rate/100)*len_year),2)

#calculating compound interest using formula
compound_interest = round(principal*(1+(interest_rate/100)/num_deposits)**(num_deposits*len_year),2)

#printing final results
print("\nSimple Interest: "+str(simple_interest))
print("Compound Interest: "+str(compound_interest))
