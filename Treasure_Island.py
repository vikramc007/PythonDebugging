print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
which_way =  input('Do you want to go "left" or "right"? ').lower()
if not which_way == "left":
   print("You fell into a hole. Game over!")
elif which_way == "left":
    how_to_cross_lake = input("You arrived to a lake. Do you want to swim, "
                              "or do you want to wait for a boat to cross the lake?  ").lower()
    if not how_to_cross_lake == "wait":
        print("You are attacked by a trout. Game over!")
    elif how_to_cross_lake == "wait":
        which_color = input("You have arrived at the island unharmed. There is a house with 3 doors, "
                            "one red, one yellow and one blue. Which color do you choose?  ").lower()
        if which_color == "red":
           print("You are Burned by fire. Game over!")
        elif which_color == "blue":
           print("You are eaten by a beast. Game over!")
        elif not which_color == "yellow":
            print("Game over!")
        else:
           print("You Win!")
