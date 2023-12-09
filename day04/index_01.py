input = open('input.txt', 'r')
lines = []

#Split Lines of Input into its own array
for l in input:
    lines.append(l)

results = []
cardNo = 0
pipePos = 0
colonPos = 0
for cardSet in lines:
    #Reset
    winningStr = ""
    ourCardStr = ""
    winningNumbers = []
    ourNumbers = []

    cardNo += 1
    solution = 0
    matchingNumbers = []

    #Clean String
    colonPos = cardSet.index(":")
    pipePos = cardSet.index("|")
    winningStr = cardSet[colonPos+1:pipePos]
    ourCardStr = cardSet[pipePos+1:]
    winningStr = winningStr.replace("\n", "")
    ourCardStr = ourCardStr.replace("\n", "")

    #Turn String into int-list
    winningNumbers = winningStr.split(" ")
    ourNumbers = ourCardStr.split(" ")
    winningNumbers = list(filter(None, winningNumbers))
    ourNumbers = list(filter(None, ourNumbers))
    winningNumbers = [ int(x) for x in winningNumbers]
    ourNumbers = [ int(x) for x in ourNumbers]

    for winNo in winningNumbers:
        if winNo in ourNumbers:
            matchingNumbers.append(winNo)

    if len(matchingNumbers) != 0:
        solution = pow(2, len(matchingNumbers)-1)
    results.append(solution)


solution = 0
for x in results:
    solution += x
print(solution)