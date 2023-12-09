input = open('input.txt', 'r')
lines = []
numbers = ["0","1","2","3","4","5","6","7","8","9"]
solutionSum = 0

#Split Lines of Input into its own array
for l in input:
    lines.append(l)

def get_fullNumber(line, checked_x_pos, numbers):
    start_x = int(checked_x_pos)
    end_x = int(checked_x_pos)

    #Go to the furthest left/start of the number
    while start_x >= 0 and line[start_x-1] in numbers:
        start_x -= 1

    #Go to the furthest right/end of the number
    while end_x < len(line) and line[end_x+1] in numbers:
        end_x += 1

    print(line[:start_x] + "\x1b[6;30;42m" + line[start_x:end_x+1] + "\x1b[0m" + line[end_x+1:])
    print("---")
    #Correct offset to include last digit
    end_x = end_x + 1
    return line[start_x:end_x]

#lines[y][x]
for y in range(len(lines)-1):
    for x in range(len(lines[y])-1):

        #Check if symbol
        if lines[y][x] != "." and lines[y][x] not in numbers:
            #Check if a number is around the checked pos while staying in bounds
            print(lines[y][:x] + "\033[91m" + lines[y][x] + "\033[0m" + lines[y][x+1:])
            #up
            if y-1 >= 0 and lines[y-1][x] in numbers:
                solutionSum += int(get_fullNumber(lines[y-1], x, numbers))
                print("up")
            #left
            elif x-1 >= 0 and lines[y][x-1] in numbers:
                solutionSum = int(get_fullNumber(lines[y], x-1, numbers))
                print("left")
            #down
            elif y+1 < len(lines) and lines[y+1][x] in numbers:
                solutionSum += int(get_fullNumber(lines[y+1], x, numbers))
                print("down")
            #right
            elif x+1 < len(lines[y]) and lines[y][x+1] in numbers:
                solutionSum += int(get_fullNumber(lines[y], x+1, numbers))
                print("right")
            #up-left
            elif y-1 >= 0 and x-1 >= 0 and lines[y-1][x-1] in numbers:
                solutionSum += int(get_fullNumber(lines[y-1], x-1, numbers))
                print("up-left")
            #up-right
            elif y-1 >= 0 and x+1 < len(lines[y]) and lines[y-1][x+1] in numbers:
                solutionSum += int(get_fullNumber(lines[y-1], x+1, numbers))
                print("up-right")
            #down-left
            elif y+1 < len(lines) and x-1 >= 0 and lines[y+1][x-1] in numbers:
                solutionSum += int(get_fullNumber(lines[y+1], x-1, numbers))
                print("down-left")
            #down-right
            elif y+1 < len(lines) and x+1 < len(lines[y]) and lines[y+1][x+1] in numbers:
                solutionSum += int(get_fullNumber(lines[y+1], x+1, numbers))
                print("down-right")

print(solutionSum)