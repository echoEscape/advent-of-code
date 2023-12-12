input = open('test_input.txt', 'r')
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
        directions[key] = ranges
        ranges = [] #Reset ranges for new direction
    else:
        ranges.append(line.split(" "))

#---
seedSteps = {}
for seedNr in seeds:
    seedSteps[seedNr] = []

for seed in seeds:
    tempSeed = int(seed)
    for key in directions:
        alreadyFound = False
        for rule in directions[key]:
            offset = 0
            #rule[0] = destination, rule[1] = source, rule[2] = range
            dest_min = int(rule[0])
            dest_max = int(rule[0]) + (int(rule[2])-1) #-1 because the start value counts too. Range of 2 means (start:25), 25 and 26 then and not 27 which would happen if I'd do a +2(range)
            src_min = int(rule[1])
            src_max = int(rule[1]) + (int(rule[2])-1)

            '''print(f"Seed: {seed}")
            print(f"Destination: {rule[0]}")
            print(f"Source: {rule[1]}")
            print(f"Last match: {tempSeed}")'''

            if alreadyFound == False and tempSeed >= src_min and tempSeed <= src_max:
                alreadyFound = True #Set true if sourcenumber can be found within the range
                offset = tempSeed - src_min
                nextStep = dest_min + offset
        if alreadyFound == False:   #If no translation can be found, the destination is = seedNo
            nextStep = int(tempSeed)

        currSteps = seedSteps[str(seed)]
        currSteps.append(nextStep)
        seedSteps[str(seed)] = currSteps

        tempSeed = nextStep
        #print("---")

print(seedSteps)
