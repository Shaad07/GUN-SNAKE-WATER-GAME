import random
computer = random.randint(0,2)

player = int(input("ENTER YJOUR CHOICE :\npress '0' for snake\npress '1' for water \npress '2' for gun : \n"))

if(player == 0):
    print("You chooses snake\n")
elif(player == 1):
    print("You chooses water\n")
elif(player == 2):
    print("You chooses gun\n")

else:
    print("invalid choice\n")        

if(computer == 0):
    print("Computer chooses snake\n")
elif(computer == 1):
    print("Computer chooses water\n")
else:
    print("Computer chooses gun\n")        



if(computer == 0 and player == 0):
    print("Game is draw")

elif(computer == 1 and player == 1):
    print("Game is draw")

elif(computer == 2 and player == 2):
    print("Game is draw")

elif(computer ==  player):
    print("Game is draw")



# elif(computer == 0):
#     if(player == 1):
#         print("Computer wins")
#     else:
#         print("Congartulations You win ")
    
# elif(computer == 1):
#     if(player == 2):
#         print("Computer wins")
#     else:
#         print("Congartulations You win ")

# elif(computer == 2):
#     if(player == 0):
#         print("Computer wins")
#     else:
#         print("Congartulations You win ")

else:
    print("Wrong choice ")





