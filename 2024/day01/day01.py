input = open('input_01.txt', 'r')
lines = [[],[]]
for l in input:
    temp_id1, temp_id2 = l.split()

    lines[0].append(int(temp_id1))
    lines[1].append(int(temp_id2))

# Task one: Sort from lowest to highest and compare the values of both lists in the same index.
# Summarize the differences between all numbers

# Sort each individual list from lowest to highest to not deal with keeping track of an index
lines[0] = sorted(lines[0])
lines[1] = sorted(lines[1])

result = 0
for x in range(len(lines[0])):
    diff = 0
    diff = abs(lines[1][x] - lines[0][x]) #Get absolute difference to remove negative values
    result = result + diff
print(result)


#Task 2:
# Count the occurrences of the values of the 1st list in the 2nd list and multiply.
# e.g. Number 3 (left) appears 3 times in right list so 3*3 = 9. 
# At the end return the sum of all multiplied occurrences.

result2 = 0
for needle in lines[0]:
    occur = 0
    for hay in lines[1]:
        if hay == needle:
            occur += 1
    result2 = result2 + (needle * occur)

print(result2)

