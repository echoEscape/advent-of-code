input = open('input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))
lines = list(filter(None, lines))

#--- Create list of seed numbers
seeds = lines.pop(0) #Remove first line of the seed input to not mess up the dict creation
seeds = seeds.replace("seeds: ", "")
seeds = seeds.split(" ")

#--- Create dictionary
# dict = [key: [destination, source, range], [destination, source, range], key: ... ]
directions = {}
key = ""
ranges = []
for line in lines:
    if line[0].isalpha(): #If first symbol is a letter it's the sorting name and not the number directions/values
        key = line
        ranges = [] #Reset ranges for new direction
    else:
        ranges.append(line.split(" "))
        directions[key] = ranges

#--- Create list of seeds to start from
seedSteps = {}
for seedNr in seeds:
    seedSteps[seedNr] = []

for seed in seeds:
    tempSeed = int(seed)
    for key in directions:
        alreadyFound = False
        nextStep = 0
        for rule in directions[key]:
            offset = 0
            #rule[0] = destination, rule[1] = source, rule[2] = range
            dest_min = int(rule[0])
            src_min = int(rule[1])
            src_max = int(rule[1]) + (int(rule[2])-1)

            '''print(f"Seed: {seed}")
            print(f"Destination: {rule[0]}")
            print(f"Source: {rule[1]}")
            print(f"Last match: {tempSeed}")'''

            if alreadyFound == False and tempSeed >= src_min and tempSeed <= src_max:
                alreadyFound = True             #Set true if sourcenumber can be found within the range
                offset = tempSeed - src_min     #Essentially get the position of the value in the rangelist. e.g. 3rd number in the range
                nextStep = dest_min + offset    #From the example one line above: get the third value in the range for the destination
        if alreadyFound == False:       #If no translation can be found, destination = seedNo
            nextStep = int(tempSeed)    #Last Searched value/source stays the same for the next key if value cant be found in range

        currSteps = seedSteps[str(seed)]    #Grab List of steps from seed-key
        currSteps.append(nextStep)          #Add next step to grabbed list
        seedSteps[str(seed)] = currSteps    #Add new list back to the key with added step

        tempSeed = nextStep #TempSeed: The SourceNo for the next key

#Part 1 - Print lowest location number
lowestLocation = 999999999999999999999999999999999999999
for key in seedSteps:
    locationNumber = int(seedSteps[key][len(seedSteps[key])-1])
    if locationNumber < lowestLocation:
        lowestLocation = locationNumber

print(lowestLocation)