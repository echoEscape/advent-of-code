input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l.replace("\n", ""))

def printMap(mapStr, visitedCoords):
  for y in range(len(mapStr)):
    yLine = ''
    for x in range(len(mapStr[y])):
      visBool = False
      for key, value in visitedCoords.items():
        for visited in value:
          if visited[0] == y and visited[1] == x:
            yLine += 'x'
            visBool = True

      if mapStr[y][x] == '#':
        yLine += '#'
      elif visBool == False:
        yLine += '.'
    print(yLine)

def getInitPos(needle, haystack):
  for yPos in range(len(haystack)):
    for xPos in range(len(haystack[yPos])):
      if haystack[yPos][xPos] == needle:
        return [yPos,xPos]

def checkInBounds(mapStr, currPos):
  maxYLen = len(mapStr)-1
  maxXLen = len(mapStr[0])-1

  if currPos[0] >= maxYLen or currPos[0] < 0:
    return False
  elif currPos[1] >= maxXLen or currPos[1] < 0:
    return False
  else:
    return True

def changeDirection(currDir):
  if currDir == 'up':
    return 'right'
  elif currDir == 'right':
    return 'down'
  elif currDir == 'down':
    return 'left'
  elif currDir == 'left':
    return 'up'
  else:
    return 'error'

def assumeNextStep(currY, currX, directions, currentDir):
  nextY = currY + directions[currentDir][0]
  nextX = currX + directions[currentDir][1]
  return nextY, nextX

def walkPath(board, visitedCoords, playerCoords, currentDir, directions):
  loop = 0
  inBounds = True

  while inBounds:
    # Assume next coordinate
    nextY, nextX = assumeNextStep(playerCoords[0], playerCoords[1], directions, currentDir)

    while board[nextY][nextX] == '#':
      currentDir = changeDirection(currentDir)
      nextY, nextX = assumeNextStep(playerCoords[0], playerCoords[1], directions, currentDir)

    inBounds = checkInBounds(board, [nextY, nextX])
    if inBounds:
      playerCoords = [nextY, nextX]
      prevY, prevX = nextY, nextX

      # Check if path has been walken in the same direction before
      if [prevY, prevX] not in visitedCoords[currentDir]:
        visitedCoords[currentDir].append([prevY, prevX])
      else:                                                                     # Task 2: Looped path detected
        loop = 1
        inBounds = False                                                        # Mis-use of variable to break out                                    
    else:
      visitedCoords[currentDir].append([nextY, nextX])                          # For task one, making sure the last step is recorded too
    
  return visitedCoords, loop

# [y,x]
directions = {'up': [-1,0],
              'right': [0,1],
              'down': [1,0],
              'left': [0,-1]}
currentDir = 'up'
playerCoords = getInitPos('^', lines)
visitedCoords = {'up':[],'right':[],'down':[],'left':[]}
visitedCoords['up'].append(playerCoords)


# Task 1: Merge dict down to unique steps taken
initialPath = walkPath(lines, visitedCoords, playerCoords, currentDir, directions)[0]

tempList = []
uniqueList = []
for key in initialPath:
  for item in initialPath[key]:
    tempList.append(item)

for item in tempList:
  if item not in uniqueList:
    uniqueList.append(item)
print(len(uniqueList))

# Task 2: Generate a unique playingboard with an obstacle at each position of the walken path, then use duplicate detection to spot looping path
loopedPaths = 0
loopedCount = 0
for key in initialPath:
  for stepCoords in initialPath[key]:
    # Reset
    playerCoords = getInitPos('^', lines)
    visitedCoords = {'up':[],'right':[],'down':[],'left':[]}
    visitedCoords['up'].append(playerCoords)
    tempMap = []
    if key != 'up' and playerCoords != stepCoords:                                         # Don't use player starting position
      tempMap = lines.copy()

      targetLine = tempMap[stepCoords[0]]
      pos = stepCoords[1]

      #print(pos)
      #print(targetLine)
      #print(targetLine[:pos])
      #print(targetLine[pos+1:])
      targetLine = targetLine[:pos] + '#' + targetLine[pos+1:]
      #print(targetLine)
      #print("---")
      tempMap[stepCoords[0]] = targetLine                                       # Replace string line with line including an obstacle

      loopedPaths = walkPath(tempMap, visitedCoords, playerCoords, currentDir, directions)
      loopedCount += loopedPaths[1]
      #if loopedPaths[1] == 1:
        #printMap(tempMap, {'up': [[0,0]]})
        #print("!!!")
        #printMap(tempMap, visitedCoords)
      #print(loopedPaths[1])
      #print("---")
#print(visitedCoords)
print(loopedCount)
#printMap(lines, visitedCoords)
