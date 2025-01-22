from xml.dom.minidom import ProcessingInstruction

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#I_have = [0, 1, 2]
Computer_has = [0, 1, 2]
I_shoot = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
Computer_shoot = random.choice(Computer_has)

game_image = [rock, paper, scissors]
#print(game_image[0])

if I_shoot == 0 and Computer_shoot == 0:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("It's a Draw!")
elif I_shoot == 0 and Computer_shoot ==1:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("You lose!")
elif I_shoot == 0 and Computer_shoot == 2:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("You Win!")
elif I_shoot==1 and Computer_shoot==0:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("You Win!")
elif I_shoot==1 and Computer_shoot==1:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print(" it is a Draw!")
elif I_shoot==1 and Computer_shoot==2:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("You loose!")
elif I_shoot==2 and Computer_shoot==0:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print(" You lose!")
elif I_shoot==2 and Computer_shoot==1:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("You win!")
elif I_shoot==2 and Computer_shoot==2:
    print(game_image[I_shoot] + "\n")
    print("Computer chose: \n")
    print(game_image[Computer_shoot] + "\n")
    print("It is a Draw!")

