input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l.replace("\n", ""))

search = ['M', 'A', 'S']                                                        # Omit "X" as first search entry as it's used at the start for the search-function in an if
directions=[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1] # [<->][^v], clockwise starting right

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
        if haystack[ySearch][xSearch] == searchStr[searchCharNo]:
          tempFoundChars += 1
        else:
          break                                                                 # Stop searching if search can't be completed
      else:
        break                                                                   # Stop searching in one direction if the search goes out of bounds
      
    if tempFoundChars == len(searchStr):                                        # Only if amount of searched characters has been reached, count as fully found in one direction
      counter += 1
  return counter

solution = 0
for yPos in range(len(lines)):
  for xPos in range(len(lines[yPos])):
    if lines[yPos][xPos] == 'X':                                                # Search in all directions starting from X
      solution += searchString(lines, [yPos,xPos], search, directions)
print(solution)