input = open('input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))

lines[0] = lines[0].split(":")
lines[1] = lines[1].split(":")
timeList = lines[0][1].strip().split("     ")
distanceList = lines[1][1].strip().split("   ")

#Part 1
amountRecordbreaks = {}
for gameNo in range(len(timeList)):
    possibleRecordbreaks = 0
    timelimit = int(timeList[gameNo])
    recordDistance = int(distanceList[gameNo])
    for timeHeld in range(timelimit):
        traveltime = timelimit - timeHeld
        traveldistance = timeHeld * traveltime
        if traveldistance > recordDistance:
            possibleRecordbreaks += 1
    amountRecordbreaks[gameNo] = possibleRecordbreaks

keys = amountRecordbreaks.keys()
result_pt1 = 1
for key in keys:
    result_pt1 *= amountRecordbreaks[key]
print(result_pt1)

#Part 2 - Takes a bit to compute
time = lines[0][1].replace(" ", "")
distance = lines[1][1].replace(" ", "")
possibleRecordbreaks_pt2 = 0
for timeHeld in range(int(time)):
        traveltime = int(time) - timeHeld
        traveldistance = timeHeld * traveltime
        if traveldistance > int(distance):
            possibleRecordbreaks_pt2 += 1

print(possibleRecordbreaks_pt2)