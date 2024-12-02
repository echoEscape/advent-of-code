input = open('input_01.txt', 'r')
lines = []
for l in input:
    tempLine = l.replace("\n", "")
    tempLine = tempLine.split()
    tempLine = list(map(int, tempLine))
    lines.append(tempLine)


# Task 1: 
# 1. The values of a line are either all increasing or decreasing
# 2. Two adjacent values of a line are allowed a difference of between 1 and 3
# Count the correct lines

# Task 2:
# If a value causes an error it can be removed from the line and be re-checked
# Count the correct lines with the "error dampener"

def checkSafety(line):
    safe = True

    # Check if List is strictly decreasing or increasing
    # Get initial direction with first pair 
    if line[0] > line[1]:
        rev = True          # desc
    elif line[0] < line[1]:
        rev = False         # asc
    else:                   
        safe = False        # No difference -> diff = 0, invalid direction

    if safe and (sorted(line, reverse=rev) == line): # sorted() catches a change in direction within the level which would be invalid
      # ---
      # Check if the difference of neighboring values is between 1 and 3
      for pos in range(len(line) - 1):
          diff = line[pos] - line[pos + 1]
          if abs(diff) < 1 or abs(diff) > 3:
              safe = False
    else:
        safe = False
    
    if safe:
        return True
    else:
        return False

# Task 1
numReports = 0
for line in lines:
    if checkSafety(line):
        numReports += 1
print(numReports)

#Task 2
# Try all iterations of a line and check if one is correct, then add to sum
numReports = 0
for line in lines:
    corrLevel = checkSafety(line)
    for pos in range(len(line)):
      tempLine = line.copy()
      tempLine.pop(pos)
      
      if corrLevel == False and checkSafety(tempLine):
          corrLevel = True
    if corrLevel:
        numReports += 1
print(numReports)
    