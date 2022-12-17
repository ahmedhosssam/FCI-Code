import random
# random.randint(0,9)

rand = random.randint(0,9)
attempts = 0

while attempts < 4 :
  choice = int(input('Enter Number between 0 and 10\n'))
  if choice == rand :
    print('Correct!')
    break
  elif choice > rand :
    print('Too high')
    attempts += 1
  elif choice < rand :
    print('Too low')
    attempts +=1
  if attempts == 4 : print('You lost!')