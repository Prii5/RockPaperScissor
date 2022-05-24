def getUserInput():
    userInput = str(input("Enter from Rock, Paper, or Scissor: ")).lower()
    while userInput not in ["rock", "paper" , "scissor"]:
        print('Not valid, Enter again')
        userInput = str(input("Enter from Rock, Paper, or Scissor: ")).lower()
    return userInput




