input = open('input_01.txt', 'r')
lines = [[],[]]
for l in input:
    temp_id, temp_coord = l.split()

    lines[0].append(temp_id)
    lines[1].append(temp_coord)

# Sort each individual list from lowest to highest
lines[0] = sorted(lines[0])
lines[1] = sorted(lines[1])

# Task one: Return the summary of the difference of each individual value of both SORTED lists
result = 0
for x in range(len(lines[0])):
    diff = 0
    diff = abs(int(lines[1][x]) - int(lines[0][x])) #Get absolute difference to remove negative values
    result = result + diff
    print(f'{lines[1][x]} - {lines[0][x]} = {diff}')

print(result)

#Task 2:
# This time, you'll need to figure out exactly how often each number from the 
# left list appears in the right list. Calculate a total similarity score by 
# adding up each number in the left list after multiplying it by the 
# number of times that number appears in the right list.
# e.g. Number 3 (left) appears 3 times in right list so 3*3 = 9. At the end get the sum of all multiplied occurrences

result2 = 0
for id in lines[0]:
    occur = 0
    for coord in lines[1]:
        if int(coord) == int(id):
            occur += 1
    result2 = result2 + (int(id) * occur)

print(result2)

