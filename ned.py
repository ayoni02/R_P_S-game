import random
def picked(pick):
    if pick == "R":
        return "Rock"
    elif pick == "S":
        return "Scissors"
    elif pick == "P":
        return "Paper"

    
played = False
system_win = "The system wins"
player_win = "You win"
tie = "It's a tie"
while played == False:
    player = ((input("Enter between R, P or S: ").upper()))
    
    system = (random.choice(["R", "P", "S"]))
    print("Player" ,picked(player), ":","CPU", picked(system))
    if player == "P" or "S" or "R":
        if player == system:
            result = tie
            print(result)
        elif player == "R" and system == "P":
            result = system_win
            print(result)
            played = True
        elif player == "R" and system == "S":
            result = player_win
            print(result)
            played = True
        elif player == "S" and system == "P":
            result = player_win
            print(result)
            played = True
        elif player == "S" and system == "R":
            result = system_win
            print(result)
            played = True
        elif player == "P" and system == "R":
            result = player_win
            print(result)
            played = True
        elif player == "P" and system == "S":
            result = system_win
            print(result)
            played = True
    else:
        print("You must enter between R, P or S:")