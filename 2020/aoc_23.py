import time

puzzleInput = """198753462"""
puzzleInput = list(puzzleInput)
for i in range(len(puzzleInput)):
    puzzleInput[i] = int(puzzleInput[i])

#milList = list(range(10, 1000001))
#puzzleInput = puzzleInput + milList

currentVal = puzzleInput[0]
currentPos = 0

starttime = time.time()
for i in range(1):
    removedCups = []
    cupsCnt = 0

    #---- REMOVE 3 AFTER currentCupPOS
    removePos = currentPos+1
    while cupsCnt < 3:
        if removePos >= len(puzzleInput):
            removePos = 0
            cupsCnt += 1
            removedCups.append(puzzleInput[removePos])
            puzzleInput.pop(removePos)

        if cupsCnt < 3:
            cupsCnt += 1
            removedCups.append(puzzleInput[removePos])
            puzzleInput.pop(removePos)

    #--- DESTINATION CUP
    destinationVal = '#'
    offset = currentVal-1           #Search one lower than the current chosen number
    while destinationVal == '#':
        if offset < 0:
            offset = max(puzzleInput)

        if offset in puzzleInput:
            destinationVal = offset
        else:
            offset -= 1

    #--- INSERT DELLIST AFTER DESTINATIONCUP
    destinationPos = puzzleInput.index(destinationVal)
    #Insert it one pos later. if it's at the end, place it at the front of the list
    #RECHECK THIS PART
    destinationPos += 1
    if destinationPos > len(puzzleInput):
        destinationPos = 0

    for i in range(len(removedCups)):
        puzzleInput.insert(i + destinationPos, removedCups[i])



    #---- DETERMINE NEW CURRENTVAL
    currentPos = puzzleInput.index(currentVal)
    currentPos += 1
    if currentPos >= len(puzzleInput):
        currentPos = 0
    currentVal = puzzleInput[currentPos]

print(time.time() - starttime)


posOne = puzzleInput.index(1)
numOne = puzzleInput[posOne+1]
numTwo = puzzleInput[posOne+2]

print(posOne)
print(puzzleInput[posOne])
print(numOne)
print(numTwo)
