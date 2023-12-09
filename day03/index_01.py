input = open('input.txt', 'r')
lines = []
numbers = ["1","2","3","4","5","6","7","8","9"]
solutionSum = 0

#Split Lines of Input into its own array
for l in input:
    lines.append(l)

def get_fullNumber(line, checked_x_pos, numbers):
    start_x = int(checked_x_pos)
    end_x = int(checked_x_pos)

    #Go to the furthest left/start of the number
    while start_x > 0 and line[start_x-1] in numbers:
        print("True 1")
        start_x -= 1

    #Go to the furthest right/end of the number
    while end_x < len(line) and line[end_x+1] in numbers:
        print("True 2")
        end_x += 1

    print(start_x)
    print(end_x)
    print(line[int(start_x):int(end_x)])

    return line[start_x:end_x]

#lines[y][x]
for y in range(len(lines)-1):
    for x in range(len(lines[y])-1):

        #Check if symbol
        if lines[y][x] != "." and lines[y][x] not in numbers:
            #Check if a number is out of bounds around the checked pos
            #up
            if y-1 >= 0 and lines[y-1][x] in numbers:
                solutionSum += int(get_fullNumber(lines[y-1], x, numbers))
            #left
            if x-1 >= 0 and lines[y][x-1] in numbers:
                solutionSum = get_fullNumber(lines[y], x-1, numbers)
            #down
            if y+1 < len(lines) and lines[y+1][x] in numbers:
                solutionSum += int(get_fullNumber(lines[y+1], x, numbers))
            #right
            if x+1 < len(lines[y]) and lines[y][x+1] in numbers:
                solutionSum += int(get_fullNumber(lines[y], x+1, numbers))
            #up-left
            if y-1 >= 0 and x-1 >= 0 and lines[y-1][x-1] in numbers:
                solutionSum += int(get_fullNumber(lines[y-1], x-1, numbers))
            #up-right
            if y-1 >= 0 and x+1 < len(lines[y-1]) and lines[y-1][x+1] in numbers:
                solutionSum += int(get_fullNumber(lines[y-1], x+1, numbers))
            #down-left
            if y+1 < len(lines) and x-1 >= 0 and lines[y+1][x-1] in numbers:
                solutionSum += int(get_fullNumber(lines[y+1], x-1, numbers))
            #down-right
            if y+1 < len(lines) and x+1 < len(lines[y]) and lines[y+1][x+1] in numbers:
                solutionSum += int(get_fullNumber(lines[y+1], x+1, numbers))

print(solutionSum)