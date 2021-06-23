#Team Chooser
#Files. 3 teams

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
teamC = []
teamAname = choice(teamNames)
teamNames.remove(teamAname)
teamBname = choice(teamNames)
teamNames.remove(teamBname)
teamCname = choice(teamNames)
teamNames.remove(teamCname)

while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)
  
  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)
  if players == []:
    break
  playerC = choice(players)
  teamC.append(playerC)
  players.remove(playerC)

file3.write("%s\n" % teamAname)
for element in teamA:
  file3.write("%s\n" % element)  

file3.write("\n")
file3.write("%s\n" % teamBname)
for element in teamB:
  file3.write("%s\n" % element) 

file3.write("\n")
file3.write("%s\n" % teamCname)
for element in teamC:
  file3.write("%s\n" % element)

print(teamAname, teamA)
print(teamBname, teamB)
print(teamCname, teamC)
