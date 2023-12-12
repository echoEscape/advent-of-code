input = open('test_input.txt', 'r')
lines = []
for l in input:
    lines.append(l.replace("\n", ""))
lines = list(filter(None, lines))

#--- Create list of seed numbers
seeds = lines.pop(0)
seeds = seeds.replace("seeds: ", "")
seeds = seeds.split(" ")

#--- Create dictionary -> Sort data input
directions = {}
key = ""
ranges = []
for line in lines:
    if line[0].isalpha():
        directions[key] = ranges
        ranges = [] #Reset ranges for new direction
        key = line
    else:
        ranges.append(line.split(" "))
del directions[""] #Remove the very first empty entry due to the start of the if line[0].isalpha()


