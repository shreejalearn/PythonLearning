import random, sys


# Dictionary of the valid quizzes available to the user.
# The key is the category and the value is the data file name.
category_datafiles = {"East": "states_east.txt",
              "West": "states_west.txt",
              "South": "states_south.txt",
              "Central": "states_central.txt",
              "All": "states_all.txt",
              }


"""
Prints out all available categories, then asks
the user to select a category to use for the quiz.

The function makes sure the user makes a valid selection before 
returning the name of the matching datafile.

"""
def get_datafile_choice():
    print("Which data file would you like to load?\nSouth All West Central East")
    #Loops to ensure user has a valid input from these choices
    while True:
        choice = input("")
        #checks user input
        if choice.lower() == 'south' or choice.lower() == 'all' or choice.lower() == 'west' or choice.lower() == 'central' or choice.lower() == 'east':
            #returns file location
            return f"states_{choice}.txt"
        else:
            print("Invalid choice, please re-enter")
            continue

      
"""
Reads the specified text file, and returns a new dictionary made from its contents.

"""
    
def read_states_into_dict(file_name):
    states_dict = {}
    #This file_name is fed in from the previous function
    file = open(file_name)
    for line in file:
        #Each state/capital combination is separated by a double colon '::'
        key, value = line.split("::")
        #Strips to remove the newline character
        states_dict[key] = value.strip("\n")
    return states_dict

"""
Using the given dictionary of state-capital pairs, 
this function implements a loop that will continue to quiz the 
user on randomly chosen states until the user types "quit" or 
correctly identifies all of the state-capitals.

Each time the user identifies a state's capital, it is removed from the game.

At the end, the function will report how many guesses were made by the user;
if the user quits before finishing all states, it also reports the fraction 
of states that were solved.
Does not return anything.
"""

def quiz(my_dict):
    #Creating tuple of the dictionary (this is so the length stays consistent since tuples are immutable and can't be changed)
    tuple_dict = tuple(my_dict)
    guesses = 0
    correct = 0

    print("\nLet's begin the quiz. Once you get a state correct, I will remove it from the list. Let's play until you get them all correct. Or, if you grow tired, enter quit to exit at any time.\nGood luck!\n")

    #Loops until dictionary is empty
    while len(my_dict) != 0:
        #Loops through every key,value pair in the dictionary
        for item in list(my_dict.keys()):
            questions = input(f"What is the capital of {item}? ")
            guesses+=1

            #If user decides to quit before the quiz ends
            if questions.lower() == "quit":
                #Shows number of guesses and the number of correct answers out of the total
                print(f"Good bye. You got {correct}/{len(tuple_dict)} correct and guessed a total of {guesses-1} times.")
                #Breaks out of the program without raising any errors
                sys.exit(0)

            #Checks if the user's input is correct
            elif questions.lower() == my_dict.get(item):
                print("Correct!")
                correct +=1
                #Deltes the item from the dictionary so the user isn't asked stuff they know again
                del my_dict[item]

            else:
                print(f"Incorrect! The capital is {my_dict.get(item)}")
    
    #Only runs when the user has completed the quiz and gotten all correct
    print(f"Wow! You got all {correct} correct in {guesses} guesses!")


#Controlling the flow of the code

def main ():
    """
    Code is provided for you. Do not change this main function.
    """
    file_name = get_datafile_choice()
    my_dict = read_states_into_dict (file_name)
    quiz (my_dict)

main()
