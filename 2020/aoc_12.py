import copy

rawDirections = """F10
N3
F7
R90
F11""".split("\n")

#directions[numberOfDirectionPair][0 -> Action][1 -> Value]
moves = [[0 for j in range(2)] for i in range(len(rawDirections))]
scores =  [['north', 0], ['east', 0], ['south', 0], ['west', 0]]
waypoint = [['north', 1], ['east', 10], ['south', 0], ['west', 0]]
for act in range(len(moves)):
    for num in range(len(moves[act])):
        action = rawDirections[act][0]
        num = rawDirections[act][1:]
        moves[act][0] = action
        moves[act][1] = int(num)


currentDirection = [0, 1]
for index in range(len(moves)):
    print(moves[index])
    print(scores)
    print(waypoint)
    print(currentDirection)
    print("---")
    change = 0
    if moves[index][0] == 'F':
        #Actually moves the ship, everything else just moves the waypoint
        for p1 in range(moves[index][1]):
            scores[int(currentDirection[0])][1] += waypoint[int(currentDirection[0])][1]
            scores[int(currentDirection[1])][1] += waypoint[int(currentDirection[1])][1]

    elif moves[index][0] == 'L':
        #Rotate the waypoints - Left
        change = moves[index][1]
        change = change / 90                    #Tells us how many steps the array gets moved around

        #Set the directions which will adjust the "score" once F gets printed
        for stepsP1 in range(int(change)):
            currentDirection[0] -= 1
            if currentDirection[0] < 0:
                currentDirection[0] = 3
        for stepsP2 in range(int(change)):
            currentDirection[1] -= 1
            if currentDirection[1] < 0:
                currentDirection[1] = 3

        #Rotate the waypoints around depending on the degree
        for arrSteps in range(0, int(change), 1):
            tempWaypoint = copy.deepcopy(waypoint)
            waypoint[0][1] = tempWaypoint[1][1]
            waypoint[1][1] = tempWaypoint[2][1]
            waypoint[2][1] = tempWaypoint[3][1]
            waypoint[3][1] = tempWaypoint[0][1]

    elif moves[index][0] == 'R':
        #Rotate the waypoints - Right
        change = moves[index][1]
        change = change / 90                    #Tells us how many steps the array gets moved around

        for stepsP1 in range(int(change)):
            currentDirection[0] += 1
            if currentDirection[0] >= 4:
                currentDirection[0] = 0
        for stepsP2 in range(int(change)):
            currentDirection[1] += 1
            if currentDirection[1] >= 4:
                currentDirection[1] = 0

        for arrSteps in range(0, int(change), 1):
            tempWaypoint = copy.deepcopy(waypoint)
            waypoint[0][1] = tempWaypoint[3][1]
            waypoint[1][1] = tempWaypoint[0][1]
            waypoint[2][1] = tempWaypoint[1][1]
            waypoint[3][1] = tempWaypoint[2][1]

    elif moves[index][0] == 'N':
        waypoint[0][1] += moves[index][1]   #Increase North position (waypoint)
        #waypoint[2][1] -= moves[index][1]
    elif moves[index][0] == 'E':
        waypoint[1][1] += moves[index][1]   #Increase East position (waypoint)
        #waypoint[3][1] -= moves[index][1]
    elif moves[index][0] == 'S':
        waypoint[2][1] += moves[index][1]   #Increase South position (waypoint)
        #waypoint[0][1] -= moves[index][1]
    elif moves[index][0] == 'W':
        waypoint[3][1] += moves[index][1]   #Increase West position (waypoint)
        #waypoint[1][1] -= moves[index][1]

    #Task1
    '''print(currentDirection)
    change = 0
    if moves[index][0] == 'F':
        #print(currentDirection)
        scores[int(currentDirection)][1] += moves[index][1]
    elif moves[index][0] == 'L':
        change = moves[index][1]
        change = change / 90

        for steps in range(int(change)):
            currentDirection -= 1
            if currentDirection < 0:
                currentDirection = 3
    elif moves[index][0] == 'R':
        change = moves[index][1]
        change = change / 90

        for steps in range(int(change)):
            currentDirection += 1
            if currentDirection >= 4:
                currentDirection = 0

    if moves[index][0] == 'N':
        scores[0][1] += moves[index][1]
    elif moves[index][0] == 'E':
        scores[1][1] += moves[index][1]
    elif moves[index][0] == 'S':
        scores[2][1] += moves[index][1]
    elif moves[index][0] == 'W':
        scores[3][1] += moves[index][1]'''


#Determine offset
#East - West
lrScore = scores[1][1]-scores[3][1]
#lrScore = scores[3][1]-scores[1][1]
#South - North
udScore = scores[2][1]-scores[0][1]
#udScore = scores[0][1]-scores[2][1]
print(lrScore + udScore)
print(currentDirection)
print(scores)
