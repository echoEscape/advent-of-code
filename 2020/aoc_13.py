busData = """1000001
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,577,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,601,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37""".split("\n")

startTime = int(busData[0])
rawData = busData[1].split(",")
validBusses = []
for i in range(len(rawData)):
    if rawData[i] != "x":
        validBusses.append(int(rawData[i]))

print(startTime)
print(validBusses)

warteZeit = ["" for i in range(len(validBusses))]
for numBus in range(len(validBusses)):
    preTime = 0
    lastTime = 0
    nextTime = 0
    waitMin = 0

    preTime = startTime % validBusses[numBus]
    lastTime = startTime - preTime
    nextTime = validBusses[numBus] + lastTime
    waitMin = nextTime - startTime

    warteZeit[numBus] = [validBusses[numBus], waitMin]

print(warteZeit)