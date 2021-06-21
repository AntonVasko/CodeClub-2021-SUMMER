#Rock, Paper, Scissors game v1

from random import randint
print('Rules:')
print('''
    *Rock blunts scissors;
    *Paper covers rock;
    *Scissors cut paper;
 ''')
r = 'o'
p = '_____'
s = '>8'

print('Make your  choose:')
print('rock(r): ', r, '\npaper(p): ', p, '\nscissors(s): ', s)
print()
player = input('rock(r), paper(p) or scissors(s)?')
if player == 'r':
  player = r
  print (player, ' vs ', end = ' ')
elif player == 'p':
  player = p
  print (player, ' vs ', end = ' ')
else:
  player = s
  print (player, ' vs ', end = ' ')

chosen = randint(1, 3)
if chosen == 1:
  computer = r
  print(r)
elif chosen == 2:
  computer = p
  print(p)
else:
  computer = s
  print(s)

if player == computer:
  print('DRAW!')
elif player == r and computer == s:
  print('Player wins!')
elif player == r and computer == p:
  print('Computer wins!')
elif player == p and computer == r:
  print('Player wins!')
elif player == p and computer == s:
  print('Computer wins!')
elif player == s and computer == p:
  print('Player wins!')  
elif player == s and computer == r:
  print('Computer wins!')  
