#Team Chooser
#Choosing lots of players. loop While
from random import choice

players = ['Harry', 'Hermione', 'Ron', 'Anton']
print(players)

teamA = []
teamB = []


while len(players) > 0:
  playerA = choice(players)
  players.remove(playerA)
  playerB = choice(players)
  players.remove(playerB)
  teamA.append(playerA)
  teamB.append(playerB)


print('Team A: ', teamA)
print('Team B', teamB)
