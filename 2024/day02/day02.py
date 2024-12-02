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
numReports = 0
for line in lines:
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
      # Check if the difference of neighboring values is between 1 and 3
      for pos in range(len(line) - 1):
          diff = line[pos] - line[pos + 1]
          if abs(diff) < 1 or abs(diff) > 3:
              safe = False
    else:
        safe = False
    
    if safe:
        numReports += 1

print(numReports)