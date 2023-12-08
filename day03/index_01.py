input = open('input.txt', 'r')
lines = []
numbers = [1,2,3,4,5,6,7,8,9]

#Split Lines of Input into its own array
for l in input:
    lines.append(l)

#lines[y][x]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        
        #Check if symbol
        if lines[y][x] != "." and lines[y][x] not in numbers:
            #Check if a number is around the symbol
            #up
            if y-1 > 0 and lines[y-1][x] in numbers:
                pass
            #down
            if y+1 < len(lines-1) and lines[y+1][x] in numbers:
                pass
            #left
            if x-1 > 0 and lines[y][x-1] in numbers:
                pass
            #right
            if x+1 < len(lines[y-1]) and lines[y][x+1] in numbers:
                pass
            #top left
            if y-1 > 0 and lines[y-1][x] in numbers and x-1 > 0 and lines[y][x-1] in numbers:
                pass
            #top right
            if y-1 > 0 and lines[y-1][x] in numbers and x+1 < len(lines[y-1]) and lines[y][x+1] in numbers:
                pass
            #bottom left
            if y+1 < len(lines-1) and lines[y+1][x] in numbers and x-1 > 0 and lines[y][x-1] in numbers:
                pass
            #bottom right
            if y+1 < len(lines-1) and lines[y+1][x] in numbers and x+1 < len(lines[y-1]) and lines[y][x+1] in numbers:
                pass