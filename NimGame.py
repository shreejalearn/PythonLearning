#Defining all pile variables with 9 stones
pile_1 = 9
pile_2 = 9
pile_3 = 9

#Setting a while loop to repeat the player choice options 
while True:
  
  print("\nPlayer 1:\n")
  
  #Nested while loop to handle errors in case someone enters an invalid option (only for player 1)
  while True:
    #Printing changing amounts of stones in each pile as user interacts with game
    print(f"Pile 1: {pile_1}")
    print(f"Pile 2: {pile_2}")
    print(f"Pile 3: {pile_3}\n")
    #input for user choice of piles and stones
    choice_pile = int(input("From which pile would you like to take? "))
    num_stones = int(input("How many stones would you like to take? "))

    #if user chooses to take stones from pile 1
    if choice_pile == 1:
      #Checking to make sure there's at least 1 stone in each pile
      if pile_1 >=1:
        #Checking to make sure the user isn't trying to take more stones than there is in the pile
        if pile_1 >=num_stones:
          #Subtracting the number of stones the user wants to draw out from the pile
          pile_1 -= num_stones
          break
        else:
          #Prints if the user is trying to select more stones than in the pile
          print("\nSorry, invalid.\n")

      #Prints if the user is trying to select a pile that is empty
      else:
        print("\nSorry, pick a different pile!\n")
        continue


    #if user chooses to take stones from pile 2    
    elif choice_pile == 2:
      #Checking to make sure there's at least 1 stone in each pile
      if pile_2 >=1:
        #Checking to make sure the user isn't trying to take more stones than there is in the pile
        if pile_2>=num_stones:
          #Subtracting the number of stones the user wants to draw out from the pile
          pile_2 -= num_stones
          break
          
        #Prints if the user is trying to select more stones than in the pile
        else:
          print("\nSorry, invalid.\n")

        #Prints if the user is trying to select a pile that is empty  
      else:
        print("\nSorry, pick a different pile!\n")
        continue

    #if user chooses to take stones from pile 3
    elif choice_pile == 3:
      #Checking to make sure there's at least 1 stone in each pile
      if pile_3 >=1:
        #Checking to make sure the user isn't trying to take more stones than there is in the pile
        if pile_3>=num_stones:
          #Subtracting the number of stones the user wants to draw out from the pile
          pile_3 -= num_stones
          break
        else:
          print("\nSorry, invalid.\n")
      #Prints if the user is trying to select a pile that is empty
      else:
        print("\nSorry, pick a different pile!\n")
        continue

    #Error handling to ensure user doesn't enter invalid option when picking which pile they want to choose stones for
    else:
      print("\nPlease enter either the correct pile number\n\n")
      continue

  #Checks if player one takes up the last stone (and loses) by checking to see if the piles are all empty after player 1's turn
  if pile_1 <= 0 and pile_2 <= 0 and pile_3 <= 0:
    print("\nYou took the last stone! Player 1 loses.")
    break


#PLAYER 1 ABOVE...PLAYER 2 BELOW


  
  print("\nPlayer 2: \n")
  #Nested while loop to handle errors in case someone enters an invalid option (only for player 2)
  while True:
    #Printing changing amounts of stones in each pile as user interacts with game
    print(f"Pile 1: {pile_1}")
    print(f"Pile 2: {pile_2}")
    print(f"Pile 3: {pile_3}\n")

     #input for user choice of piles and stones
    choice_pile = int(input("From which pile would you like to take? "))
    num_stones = int(input("How many stones would you like to take? "))

    #if user chooses to take stones from pile 1
    if choice_pile == 1:
      #Checking to make sure there's at least 1 stone in each pile
      if pile_1 >=1:
        #Checking to make sure the user isn't trying to take more stones than there is in the pile
        if pile_1 >=num_stones:
          #Subtracting the number of stones the user wants to draw out from the pile
          pile_1 -= num_stones
          break
        else:
          #Prints if the user is trying to select more stones than in the pile
          print("\nSorry, invalid.\n")

      #Prints if the user is trying to select a pile that is empty
      else:
        print("\nSorry, pick a different pile!\n\n")
        continue
        
    #if user chooses to take stones from pile 2    
    elif choice_pile == 2:
      #Checking to make sure there's at least 1 stone in each pile
      if pile_2 >=1:
        #Checking to make sure the user isn't trying to take more stones than there is in the pile
        if pile_2>=num_stones:
          #Subtracting the number of stones the user wants to draw out from the pile
          pile_2 -= num_stones
          break
          
        #Prints if the user is trying to select more stones than in the pile
        else:
          print("\nSorry, invalid.\n")

        #Prints if the user is trying to select a pile that is empty  
      else:
        print("\nSorry, pick a different pile!\n")
        continue
    
    #if user chooses to take stones from pile 3
    elif choice_pile == 3:
      #Checking to make sure there's at least 1 stone in each pile
      if pile_3 >=1:
        #Checking to make sure the user isn't trying to take more stones than there is in the pile
        if pile_3>=num_stones:
          #Subtracting the number of stones the user wants to draw out from the pile
          pile_3 -= num_stones
          break
        else:
          print("\nSorry, invalid.\n")
      #Prints if the user is trying to select a pile that is empty
      else:
        print("\nSorry, pick a different pile!\n")
        continue

    #Checks if player two takes up the last stone (and loses) by checking to see if the piles are all empty after player 2's turn
  if pile_1 <= 0 and pile_2 <= 0 and pile_3 <= 0:
    print("\nYou took the last stone! Player 2 loses.")
    break
