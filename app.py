from user_generator import getUserInput
from generator import randomGenerator


def compareFunc():
    userInput = getUserInput()
    compInput = randomGenerator()
    if userInput == compInput:
        winner = 'none'
    elif userInput == "rock":
        if compInput == "paper":
            winner = "user"
        else:
            winner = "computer"
    elif userInput == "paper":
        if compInput == "scissor":
            winner = "computer"
        else:
            winner = "user"
    elif userInput == "scissor":
        if compInput == "paper":
            winner = "user"
        else:
            winner = "computer"
    print ("\nThe user input is:", userInput.title(), "\nThe computer input is:", compInput.title())
    return winner.title()


print('***************************************************')
print("\n\n\nWelcome to the game of rock, paper, and scissor.\nWe hope you ENJOY!")
print("The winner of this round is:", compareFunc())
print('')
print("***************************************************")

