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
    
def get_gameArray(inputArr): 
    for line in inputArr:
        pullArr = []
        dataArr = []
        gameNo = get_gamenumber(line)

        #setArr -> ["3 blue, 4 red"], ["2 green"],...
        setArr = line.split(";")

        for set in setArr:
            #pullArr -> ["3 blue"], ["4 red"]
            pullArr = set.split(", ")

            for i in range(len(pullArr)):
                #dataArr[0][0][0] -> "3", dataArr[0][0][1] -> "blue"
                dataArr[gameNo][i] = pullArr[i]

    return dataArr

def check_cubeSets(dataArr, redLimit, greenLimit, blueLimit):
    redAmount = 0
    greenAmount = 0
    blueAmount = 0
    setResult = []
    gameResult = []
    gameCnt = 0
    
    #To Check all sets of win/losses I'd need to go back in the array hierachy a step further?
    for i in range(len(dataArr[gameCnt])):
        for setNo in range(len(dataArr[gameCnt])):
            if dataArr[gameCnt][setNo][0] == "red":
                redAmount += dataArr[gameCnt][setNo][1]
            elif dataArr[gameCnt][setNo][0] == "green":
                greenAmount += dataArr[gameCnt][setNo][1]
            elif dataArr[gameCnt][setNo][setNo] == "blue":
                blueAmount += dataArr[gameCnt][setNo][1]

        if redAmount <= redLimit and greenAmount <= greenLimit and blueAmount <= blueLimit:
            setResult.append("Win")
        else:
            setResult.append("Loss")

        
            
        redAmount = 0
        greenAmount = 0
        blueAmount = 0
        gameResult = []
        gameCnt += 1

dataArr = get_gameArray(lines)
print(dataArr)
