while True:
# Allows user to input option and computer randomizes choice
    import random
    choice = ['rock', 'paper', 'scissors']
    robot = (random.choice(choice))
    user = input("Rock, Paper, or Scissors? ").lower()
    print("")
#-------------------------------------------------
# Rock options of win or lose
    if user == 'rock' and robot == 'paper':
        result = "Owned by an NPC lmao. " + "User picked: " + user + " and robot picked: " + robot + "."
    elif user == 'rock' and robot == 'scissors':
        result = "GG. " + "User picked: " + user + " and robot picked: " + robot + "."
#-------------------------------------------------
# Paper options of win or lose
    elif user == 'paper' and robot == 'scissors':
        result = "Owned by an NPC lmao. " + "User picked: " + user + " and robot picked: " + robot + "."
    elif user == 'paper' and robot == 'rock':
        result = "GG. " + "User picked: " + user + " and robot picked: " + robot + "."
# -------------------------------------------------
# Scissors options of win or lose
    elif user == 'scissors' and robot == 'rock':
        result = "Owned by an NPC lmao. " + "User picked: " + user + " and robot picked: " + robot + "."
    elif user == 'scissors' and robot == 'paper':
        result = "GG. " + "User picked: " + user + " and robot picked: " + robot + "."
#-------------------------------------------------
# Putting random words
    elif user is not 'rock' or user is not 'paper' or user is not 'scissors':
        result = "Bro play the game."
#-------------------------------------------------
# Ties
    else:
        result = 'Tie! User picked: ' + user + ' and Robot picked: ' + robot +'.'
    print(result)
    print("-----------------------------")