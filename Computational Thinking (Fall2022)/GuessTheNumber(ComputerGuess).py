import random

rand = random.randint(0,9)
attempts = 0

print('Think of a number and I will guess it!\n')

while attempts < 4:
  randChange = random.randint(1,3)
  print('Is ' + str(rand) + ' too high (H) , too low (L) , or correct (C) ?\n')
  choice = input('')
  if choice == 'H':
    attempts += 1
    rand -= randChange
    print('Is ' + str(rand) + ' too high (H) , too low (L) , or correct (C) ?\n')
    choice = input('')
  elif choice == 'L':
    attempts += 1
    rand += randChange
    print('Is ' + str(rand) + ' too high (H) , too low (L) , or correct (C) ?\n')
    choice = input('')
  elif choice == 'C':
    print('YAY!! I Guessed it ! , ' + str(rand) + ' Is Correct!!')
    break
  if attempts == 4: print('Ops! I lost :(')
  