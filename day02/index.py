input = open('input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

gameResults = []
powerLevels = []

for game in lines:
    game = game[game.find(": ")+2:]
    pull = game.split("; ")

    #Part 1
    #If any set of number+color is False, the entire game doesnt get counted
    valid = True #Set placeholder

    #Part 2
    #Add up the power level in a loop of one game by grabbing the biggest number for each color
    plRed = 0
    plGreen = 0
    plBlue = 0
    for p in pull:
        cubes = p.split(", ")
        cubeset = []

        for c in cubes:
            cubeset.append(c.split(" "))

        #PART 1 - Check Validity of amount+color ratio
        for cube in cubeset:
            if cube[1] == "red" and int(cube[0]) > 12: 
                valid = False
            elif cube[1] == "green" and int(cube[0]) > 13:
                valid = False
            elif cube[1] == "blue" and int(cube[0]) > 14:
                valid = False
        
        #Part 2
        for cube in cubeset:
            if cube[1] == "red" and int(cube[0]) > plRed: 
                plRed = int(cube[0])
            elif cube[1] == "green" and int(cube[0]) > plGreen:
                plGreen = int(cube[0])
            elif cube[1] == "blue" and int(cube[0]) > plBlue:
                plBlue = int(cube[0])
        
    #Part 1
    gameResults.append(valid)
    #Part 2
    powerLevels.append(plRed*plGreen*plBlue)

score = 0
plScore = 0
for i in range(len(gameResults)):
    if gameResults[i] == True:
        score = score + (i+1)
        plScore = plScore + powerLevels[i]
print(score)
print(plScore)