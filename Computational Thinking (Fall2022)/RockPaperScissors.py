import random

choices = ['r', 'p', 's']

attempts = 0
userScore = 0
computerScore = 0

while attempts < 4 :
  randChoice = random.choice(choices)
  userChoice = input("What's your Choice ? 'r' for rock , 'p' for paper , 's' for scissors\n")
  if userChoice == 'r' :

    if randChoice == 'r':
      print('tie')
      attempts += 1
    elif randChoice == 'p':
      print('You Lost!')
      attempts += 1
      computerScore += 1
    elif randChoice == 's':
      print('You Won')
      attempts += 1
      userScore += 1
    attempts += 1

  elif userChoice == 'p' :

    if randChoice == 'r':
      print('You Won!')
      userScore += 1
    elif randChoice == 'p':
      print('Tie!')
    elif randChoice == 's':
      print('You Lost!')
      computerScore += 1
    attempts += 1

  elif userChoice == 's':

    if randChoice == 'r':
      print('You Lost!')
      computerScore += 1
    elif randChoice == 'p':
      print('You Won!')
      userScore += 1
    elif randChoice == 's':
      print('Tie!')
    attempts += 1

if userScore > computerScore :
  print('Congrats!! You Won against the computer')
else :
  print('You Lost against the computer :((')