#Rock, Paper, Scissors game

from random import randint
r = 'o'
p = '_____'
s = '>8'
print('rock: ', r, '\npaper: ', p, '\nscissors: ', s)
player = input('rock(r), paper(p) or scissors(s)?')
print (player, ' vs ', end = ' ')
chosen = randint(1, 3)
#print(chosen)
if chosen == 1:
  computer = 'r'
elif chosen == 2:
  computer = 'p'
else:
  computer = 's'
print(computer)

if player == computer:
  print('DRAW!')
elif player == 'r' and computer == 's':
  print('Player wins!')
elif player == 'r' and computer == 'p':
  print('Computer wins!')
elif player == 'p' and computer == 'r':
  print('Player wins!')
elif player == 'p' and computer == 's':
  print('Computer wins!')
elif player == 's' and computer == 'p':
  print('Player wins!')  
elif player == 's' and computer == 'r':
  print('Computer wins!')  
