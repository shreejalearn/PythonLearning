#Used for generating a random number which is translated to either rock or paper or scissor
import random

#Setting the main variables for score tracking
comp_score = 0
player_score = 0

#Ensures that the loop breaks when either the computer or the player have a score of 5 since it's instructing the loop to only run while both the players' scores are less than 5
while player_score != 5 and comp_score != 5:

    #Player choice
    choice = input("Please enter your choice 'r'ock, 'p'aper, or 's'cissors? ")

    #A loop to ask the user to enter their choice again in case of a misclick or invalid entry
    if choice != 'r' and choice != 's' and choice != "p":
        print("\nInvalid key.\n")
        #Keyword to rerun the loop
        continue

    #Continuing if the user choice of rock, paper, or scissor is valid
    else:
        #random number
        comp_choice = random.randint(1, 3)

        #Substituting user choice value to rock instead of r
        if choice == 'r':
            choice = "rock"
        #Substituting user choice value to paper instead of rp
        elif choice == 'p':
            choice = "paper"
        #Substituting user choice value to scissor instead of s
        else:
            choice = "scissor"

        #Substituting random number generated (1) to rock
        if comp_choice == 1:
            comp_choice = "rock"
        #Substituting random number generated (2) to paper
        elif comp_choice == 2:
            comp_choice = "paper"
        #Substituting random number generated (3) to scissor
        else:
            comp_choice = "scissor"

        print(f"\nYou chose {choice}. The computer chose {comp_choice}.")

        #Listing all the possible conditions with or statements that might cause the result of a tie
        if comp_choice == "rock" and choice == "rock" or comp_choice == "paper" and choice == "paper" or comp_choice == "scissor" and choice == "scissor":
            print("\tYou tied!\n")

            #Listing all the possible conditions with or statements that might cause the result of the computer winning
        elif comp_choice == "rock" and choice == "scissor" or comp_choice == "paper" and choice == "rock" or comp_choice == "scissor" and choice == "paper":
            print("\tYou lost!\n")
            #Adding to computer score
            comp_score += 1

        #With all other possibilities taken care of in previous loop, this is printed when it's not a tie or the computer's win
        else:
            print("\tYou win!\n")
            #Adding to player score
            player_score += 1

        print("Score:")
        print(f"You: {player_score}\tComputer: {comp_score}\n")

#Once either the player or the computer has at least 5 wins, it breaks out of the loop and prints either of the statements depending on who has the higher score, the computer or the player_score

if player_score > comp_score:
    print("\nCONGRATS!! YOU WON THE MATCH!")
else:
    print("\nThe Computer won this match!")
