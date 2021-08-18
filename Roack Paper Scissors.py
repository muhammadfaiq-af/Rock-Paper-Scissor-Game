import random # I have Imported a Bulit in Lib in Python Random
Game_List = ['Rock' , 'Paper' , 'Scissors'] # Initialize a List

Computer = c =  0  # Initialize Computer with 0 
Player = p = 0  # Initialize Player with 0

print("Score : Computer" + str(c) + "Score : Player" + str(p))

run = True 

while run : # Loop
    Computer_Choice = random.choice(Game_List)  # Computer Will radomly Choice between 3 Names
    Player = input('Rock , Paper, Scissors or Qiut :    ')

    if Player == Computer_Choice: # If The choice is Same of Both Computer Nd Player so the Game Wil be Tie
        print("Tie")
    elif Player == 'Rock':
        if Computer_Choice == 'Scicssors': 
            print("Player Won")
            p += 1
        else:
            print("Computer Won")
            c += 1

    elif Player == 'Paper':
        if Computer_Choice == "Rock":
            print("Computer Won")
            c += 1
        else:
            print("Player Won")
            p =+ 1

    elif Player == 'Scissors':
        if Computer_Choice == 'Paper':
            print("Player Won")
            p += 1
        else:
            print("Computer Won")
            c += 1

    elif Player == 'Quit': # If Player Type Quit so The Game will be Over 
        break
    else:
        print("Wrong Command")
    print("Player Command" + Player)
    print("Compuer : " + Computer_Choice)
    print("")
    print("Score : Computer" + str(c) + "Score Player" + str(p))