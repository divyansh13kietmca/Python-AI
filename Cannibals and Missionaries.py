
Missionary = int(input("Enter the number of the missionary: "))
Cannibal = int(input("Enter the number of the Cannibal: "))

# condition of win is if the Missionary are to the next side without eaten
Place_2 = [0,0] 
moving_Missionary = Missionary
moving_Cannibal = Cannibal
boat_location = 0 #to check the place where the boat currently is: 0 -> Place 1 and 1 -> Place 2
rules_used = {}
count = 0

while Place_2[0] !=  Missionary or Place_2[1] != Cannibal: #Place_2[1] is Cannibal Count and Place_2[0] is Missionary Count

    if moving_Cannibal < 0 or moving_Missionary < 0 or moving_Cannibal > 3 or moving_Missionary > 3: #checking for wrong calculations
        print("-"*50)
        print("Wrong Move: They cannot be below 0 or above 3")
        print("-"*50)
        break

    elif moving_Cannibal > moving_Missionary or (Place_2[1] > Place_2[0] and Place_2[0] != 0): #checking to see the if cannibals are more than missionary
        print("-"*50)
        print("Wrong Move: The Cannibals ate the Missionaries")
        print("-"*50)
        break
    
    elif moving_Missionary == 0 and moving_Cannibal == 0 and Place_2[0] == 3 and Place_2[1] == 3: #win condition--> Everyone arrived alive and well
        print("-"*50)
        print("\n You Win \n")
        print("-"*50)
        break
        
    else:
        print("Rule 1: ( Moving 1 Missionary and 1 Cannibal ) Place 1 ---> Place 2")
        print("Rule 2: ( Moving 2 Missionaries ) Place 1 ---> Place 2")
        print("Rule 3: ( Moving 2 Cannibals ) Place 1 ---> Place 2")
        print("Rule 4: ( Moving 1 Missionary ) Place 2 ---> Place 1")
        print("Rule 5: ( Moving 1 Cannibal ) Place 2 ---> Place 1")
        print("Rule 6: ( Moving 1 Missionary and 1 Cannibal ) Place 2 ---> Place 1")
        print("Rule 7: ( Moving 2 Missionary ) Place 2 ---> Place 1")
        print("Rule 8: ( Moving 2 Cannibals ) Place 2 ---> Place 1")

        game_rule = int(input("Enter the rule to use: ")) #Input for rules which determine the path of game
        print()
        
        if boat_location == 0 and game_rule > 3: #Checking for use of place 1 rules if boat in place 1
            print("\nBoat is in Place 1. So this rule cannot be used: \n Try Again\n")
            continue
        elif boat_location == 1 and game_rule < 4: #Checking for use of place 2 rules if boat in place 2
            print("\nBoat is in Place 2. So this rule cannot be used \n Try Again\n")
            continue


        #moving from place 1 to place 2 
        elif game_rule == 1:  #1 M - 1 C
            print("( Moving 1 Missionary and 1 Cannibal ) Place 1 ---> Place 2")
            moving_Missionary -= 1
            moving_Cannibal -= 1
            Place_2[0] += 1
            Place_2[1] += 1

        elif game_rule == 2: # 2 M
            print("( Moving 2 Missionaries ) Place 1 ---> Place 2")
            moving_Missionary -= 2
            Place_2[0] += 2

        elif game_rule == 3: # 2 C
            print("( Moving 2 Cannibals ) Place 1 ---> Place 2")
            moving_Cannibal -= 2
            Place_2[1] += 2


        #moving from place 2 to place 1 
        elif game_rule == 4: # 1 M    
            print("( Moving 1 Missionary ) Place 2 ---> Place 1")
            moving_Missionary -= 1
            Place_2[0] = -1

        elif game_rule == 5: # 1 C
            print("( Moving 1 Cannibal ) Place 2 ---> Place 1")
            moving_Cannibal += 1
            Place_2[1] -= 1


        elif game_rule == 6: # 1 M -- 1 C
            print("( Moving 1 Missionary and 1 Cannibal ) Place 2 ---> Place 1")
            moving_Missionary +=1
            moving_Cannibal += 1
            Place_2[0] -= 1
            Place_2[1] -= 1
    
        elif game_rule == 7: # 2 M
            print("( Moving 2 Missionary ) Place 2 ---> Place 1")
            moving_Missionary += 2
            Place_2[0] -= 2

        elif game_rule == 8: # 2 C 
            print("( Moving 2 Cannibals ) Place 2 ---> Place 1")
            moving_Cannibal -= 2
            Place_2[1] -= 2

        print(f"Missionary = {moving_Missionary} and Cannibal = {moving_Cannibal} in place 1")    
        print(f"Missionary = {Place_2[0]} and Cannibal = {Place_2[1]} in place 2\n")    
        
        # Saving the rules used by the player in the dictionary rules_used.
        if game_rule in rules_used.keys():
            rules_used[game_rule] += 1
        else:
            rules_used[game_rule] = 1
        
        #Changing the boat_location variable according to the rule used
        if game_rule < 4:
            boat_location = 1
        else:
            boat_location = 0

        # Counting the steps used in playing the game
        count += 1


#Printing the required output
print(f"\nSteps Needed: {count}\n")
for rule in rules_used.keys():
    print(f"Rule {rule} is used {rules_used[rule]} times")