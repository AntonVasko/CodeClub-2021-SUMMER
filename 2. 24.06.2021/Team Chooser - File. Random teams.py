#Team Chooser
#Files. Teams random

from random import choice

players = []
teamNames = []
file = open('players.txt', 'r')
players = file.read().splitlines()
file = open('teams.txt', 'r')
teamNames = file.read().splitlines()

print(players)
print(teamNames)

teamA = []
teamB = []
teamAname = choice(teamNames)
teamNames.remove(teamAname)
teamBname = choice(teamNames)
teamNames.remove(teamBname)


while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)
  if players == []:
    break
  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)
  
print(teamAname, teamA)
print(teamBname, teamB)
