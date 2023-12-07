input = open('input.txt', 'r')
lines = []

#Split Lines of Input into its own array
for l in input:
    lines.append(l)

def get_gamenumber(line):
    try:
        start = line.index("Game ") + len("Game ")
        end = line.index(":", start )
        return line[start:end]
    except ValueError:
        return ""
    
def get_pullsOfCubes(line):
    gameArr = []
    newStr = ""

    gamePos = line.find(":")
    newStr = line[gamePos+2:-1]

    gameArr = newStr.split("; ")

    return gameArr

    
def check_pulls(lines, blueLimit, greenLimit, redLimit):
    setArr = []
    cubeArr = []

    for line in lines:
        currGame = get_gamenumber(line)
        pullsArr = get_pullsOfCubes(line)

        for set in pullsArr:
            setArr.append(set.split(", "))
            print(setArr)
            cubeArr = cubes.split(" ")
            #print(currGame)
            #print(setArr)

            blueCube = 0
            greenCube = 0
            redCube = 0
            for cube in cubeArr:
                if cube[1] == "blue":
                    blueCube += int(cube[0])
                elif cube[1] == "green":
                    greenCube += int(cube[0])
                elif cube[1] == "red":
                    redCube += int(cube[0])
                
check_pulls(lines, 14, 13, 12)



