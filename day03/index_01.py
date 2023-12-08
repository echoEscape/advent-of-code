input = open('input.txt', 'r')
lines = []
numbers = [1,2,3,4,5,6,7,8,9]

#Split Lines of Input into its own array
for l in input:
    lines.append(l)

def get_fullNumber(line, checked_x_pos):
    start_x = checked_x_pos
    end_x = 0
    
    #Go to the furthest left/start of the number
    while start_x > 0 and line[start_x] in numbers:
        start_x -= 1

    while end_x < len(line)-1 and line[end_x] in numbers:
        end_x +=1

    return line[start_x:end_x]

#lines[y][x]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        
        #Check if symbol
        if lines[y][x] != "." and lines[y][x] not in numbers:
            #Check if a number is out of bounds around the checked pos
            #up
            if y-1 >= 0 and lines[y-1][x] in numbers:
                get_fullNumber(lines[y-1], x)
            #left
            if x-1 >= 0 and lines[y][x-1] in numbers:
                get_fullNumber(lines[y], x-1)
            #down
            if y+1 < len(lines[y])-1 and lines[y+1][x] in numbers:
                get_fullNumber(lines[y+1], x)
            #right
            if x+1 < len(lines[y][x])-1 and lines[y][x+1] in numbers:
                get_fullNumber(lines[y], x+1)
            #up-left
            if y-1 >= 0 and x-1 >= 0 and lines[y-1][x-1] in numbers:
                get_fullNumber(lines[y-1], x-1)
            #up-right
            if y-1 >= 0 and x+1 < len(lines[y][x])-1 and lines[y-1][x+1] in numbers:
                get_fullNumber(lines[y-1], x+1)
            #down-left
            if y+1 < len(lines[y])-1 and x-1 >= 0 and lines[y+1][x-1] in numbers:
                get_fullNumber(lines[y+1], x-1)
            #down-right
            if y+1 < len(lines[y])-1 and x+1 < len(lines[y][x])-1 and lines[y+1][x+1] in numbers:
                get_fullNumber(lines[y+1], x+1)

