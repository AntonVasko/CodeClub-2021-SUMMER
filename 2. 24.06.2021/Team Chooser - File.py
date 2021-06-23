#Team Chooser
#File
from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

print(players)


teamA = []
teamB = []


while len(players) > 0:
  playerA = choice(players)
  players.remove(playerA)
  if players == []:
    break
  playerB = choice(players)
  players.remove(playerB)
  teamA.append(playerA)
  teamB.append(playerB)
  
  


print('Team A: ', teamA)
print('Team B', teamB)
