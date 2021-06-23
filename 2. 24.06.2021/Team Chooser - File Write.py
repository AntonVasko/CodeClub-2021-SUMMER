#Team Chooser
#Files. Write file

from random import choice

players = []
teamNames = []
file1 = open('players.txt', 'r')
players = file1.read().splitlines()
file2 = open('teams.txt', 'r')
teamNames = file2.read().splitlines()
file3 = open('list_teams.txt', 'w')

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

file3.write("%s\n" % teamAname)
for element in teamA:
  file3.write("%s\n" % element)  
file3.write("\n")
file3.write("%s\n" % teamBname)
for element in teamB:
  file3.write("%s\n" % element) 

print(teamAname, teamA)
print(teamBname, teamB)
