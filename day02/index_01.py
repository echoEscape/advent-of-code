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
    roundArr = []
    newStr = ""

    gamePos = line.find(":")
    newStr = line[gamePos+2:-1]

    roundArr = newStr.split("; ")

    return roundArr

    
def check_possiblePulls(gameStr):
    setArr = []
    cubeArr = []
    for set in gameStr:
        setArr.append(set.split(", "))
        cubeArr = setArr.split(" ")

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
                
            




