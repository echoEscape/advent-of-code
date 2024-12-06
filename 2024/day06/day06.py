input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l.replace("\n", ""))

def printMap(mapStr, visitedCoords):
  for y in range(len(mapStr)):
    yLine = ''
    for x in range(len(mapStr[y])):
      visBool = False
      for visited in visitedCoords:
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

def assumeNextStep(currY, currX, directions):
  nextY = currY + directions[currentDir][0]
  nextX = currX + directions[currentDir][1]
  return nextY, nextX

# [y,x]
directions = {'up': [-1,0],
              'right': [0,1],
              'down': [1,0],
              'left': [0,-1]}
currentDir = 'up'
visitedCoords = []
playerCoords = getInitPos('^', lines)
visitedCoords.append(playerCoords)
inBounds = True


while inBounds:
  # Assume next coordinate
  nextY, nextX = assumeNextStep(playerCoords[0], playerCoords[1], directions)

  while lines[nextY][nextX] == '#':
    #printMap(lines, visitedCoords)
    #print("")
    currentDir = changeDirection(currentDir)
    nextY, nextX = assumeNextStep(playerCoords[0], playerCoords[1], directions)

  inBounds = checkInBounds(lines, [nextY, nextX])
  if inBounds:
    playerCoords = [nextY, nextX]
    prevY, prevX = nextY, nextX
    if [prevY, prevX] not in visitedCoords:
      visitedCoords.append([prevY, prevX])
  else:
    visitedCoords.append([nextY, nextX])


  
#printMap(lines, visitedCoords)
#print(visitedCoords)
print(len(visitedCoords))
