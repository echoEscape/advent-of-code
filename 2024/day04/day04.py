input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l.replace("\n", ""))

search = ['M', 'A', 'S']                                                        # Omit "X" as first search entry as it's used at the start for the search-function in an if
searchTwo = ['A', 'S']                                                          # Omit "M" as first search character as it's used at the start for the search-function in an if
directions=[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1] # [<->][^v], clockwise starting right
crossDirections = [[1, -1], [-1, 1]], [[1, 1], [-1, -1]]                            # [<->][^v], top-right & bottom-left, top-left & bottom-right

# Task 1
def searchString(haystack, startCoords, searchStr, dirControls):
  counter = 0
  yPos = startCoords[0]
  xPos = startCoords[1]
  maxColLen = len(haystack)
  maxRowLen = len(haystack[xPos])
  
  for coordType in range(len(dirControls)):                                     # Check one direction for M, A, X before checking the next
    tempFoundChars = 0
    for searchCharNo in range(len(searchStr)):                                  # First loop search for "M" with offset 1, second for "A" with offset 2,...                                                           
      yOffset = dirControls[coordType][0] * (searchCharNo+1)
      xOffset = dirControls[coordType][1] * (searchCharNo+1)
      ySearch = yPos + yOffset
      xSearch = xPos + xOffset

      #Out of Bounds Check
      if (ySearch < maxColLen and ySearch >= 0) and (xSearch < maxRowLen and xSearch >= 0):
        if haystack[ySearch][xSearch] == searchStr[searchCharNo]:               # If expected character is in the searched coordinates True
          tempFoundChars += 1
        else:
          break                                                                 # Stop searching if search can't be completed
      else:
        break                                                                   # Stop searching in one direction if the search goes out of bounds
      
    if tempFoundChars == len(searchStr):                                        # Only if amount of searched characters has been reached, count as fully found in one direction
      counter += 1
  return counter

# Task 2 (Not as flexible as I'd have liked. searchStr would need to be used and the ifs in the out of bounds check would need a tracking variable. Technically it'd be over-engineered tho because the offset is always only +1 and there are only two sides to always be checked. the names could be changed though to not be so specific to M and S, but any character one would search.)
def searchCrossedString(haystack, startCoords, searchStr, crossDirCoords):
  counter = 0
  dirMatch = 0
  yPos = startCoords[0]
  xPos = startCoords[1]
  maxColLen = len(haystack)
  maxRowLen = len(haystack[xPos])
  
  for coordSet in range(len(crossDirCoords)):                                   # Check diagonal line first / and next loop \ for M and S pair
    mFound = False
    sFound = False
                                                    
    for diagonalSrc in crossDirCoords[coordSet]:                                # Check opposing sides of M and S               
      ySearch = yPos + diagonalSrc[0]
      xSearch = xPos + diagonalSrc[1]

      #Out of Bounds Check
      if (ySearch < maxColLen and ySearch >= 0) and (xSearch < maxRowLen and xSearch >= 0):
        if not mFound and haystack[ySearch][xSearch] == 'M':
          mFound = True
        if not sFound and haystack[ySearch][xSearch] == 'S':
          sFound = True
    
    if mFound and sFound:                                                       # Only if amount of searched characters has been reached, count as fully found in one direction
      dirMatch += 1

  if dirMatch == 2:                                                             # If both directions with MAS have been found, crossfound is true
    counter += 1

  return counter



solutionOne = 0
solutionTwo = 0
for yPos in range(len(lines)):
  for xPos in range(len(lines[yPos])):
    # Task 1
    if lines[yPos][xPos] == 'X':                                                # Search in all directions starting from X
      solutionOne += searchString(lines, [yPos,xPos], search, directions)

    # Task 2 - Circle around the A
    if lines[yPos][xPos] == 'A':
      solutionTwo += searchCrossedString(lines, [yPos,xPos], search, crossDirections)

print(solutionOne)
print(solutionTwo)