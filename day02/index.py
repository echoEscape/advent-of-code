input = open('input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

gameResults = []

for game in lines:
    game = game[game.find(": ")+2:]
    pull = game.split("; ")

    #If any set of number+color is False, the entire game doesnt get counted
    valid = True #Set placeholder
    for p in pull:
        cubes = p.split(", ")
        cubeset = []

        for c in cubes:
            cubeset.append(c.split(" "))

        #Check Validity of amount+color ratio
        for cube in cubeset:
            if cube[1] == "red" and int(cube[0]) > 12: 
                valid = False
            elif cube[1] == "green" and int(cube[0]) > 13:
                valid = False
            elif cube[1] == "blue" and int(cube[0]) > 14:
                valid = False

    gameResults.append(valid)

score = 0
for i in range(len(gameResults)):
    if gameResults[i] == True:
        score = score + (i+1)

print(score)