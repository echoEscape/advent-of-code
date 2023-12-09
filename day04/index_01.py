input = open('input.txt', 'r')
lines = []
points = []
cardNo = 0
pipePos = 0
colonPos = 0
globalMatchlist = []

#Split Lines of Input into its own array
for l in input:
    lines.append(l)


def clean_string(set):
    winningStr = ""
    ourCardStr = ""
    winningNumbers = []
    ourNumbers = []

    colonPos = set.index(":")
    pipePos = set.index("|")
    winningStr = set[colonPos+1:pipePos]
    ourCardStr = set[pipePos+1:]
    winningStr = winningStr.replace("\n", "")
    ourCardStr = ourCardStr.replace("\n", "")

    winningNumbers = winningStr.split(" ")
    ourNumbers = ourCardStr.split(" ")
    winningNumbers = list(filter(None, winningNumbers))
    ourNumbers = list(filter(None, ourNumbers))
    winningNumbers = [ int(x) for x in winningNumbers]
    ourNumbers = [ int(x) for x in ourNumbers]

    return winningNumbers, ourNumbers

def part_one():
    pass

for cardSet in lines:
    #Reset
    winningNumbers = []
    ourNumbers = []
    solution = 0
    loopMatchingNumbers = []
    
    cardNo += 1

    winningNumbers = clean_string(cardSet)[0]
    ourNumbers = clean_string(cardSet)[1]

    #createList with matching cardnumbers e.g. matchingNumbers[0] = [2, 3, 5]...
    for winNo in winningNumbers:
        if winNo in ourNumbers:
            loopMatchingNumbers.append(winNo)

    #part 1
    if len(loopMatchingNumbers) != 0:
        solution = pow(2, len(loopMatchingNumbers)-1)
    points.append(solution)

    globalMatchlist.append(loopMatchingNumbers)


solution = 0
for x in points:
    solution += x
print(solution)