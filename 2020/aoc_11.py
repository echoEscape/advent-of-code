#Unfinished

import copy

seatData = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")

#Create MDArray
#allSeats[column/reihe/width][row/zeile/height]
allSeats = [[0 for j in range(len(seatData[i]))] for i in range(len(seatData))]
for zeile in range(len(seatData)):
    for reihe in range(len(seatData[zeile])):
        allSeats[zeile][reihe] = seatData[zeile][reihe]

#Check all Seats
#   If L: check all seats around it -> zeile-1 bis zeile+1, reihe-1 bis reihe+1 -> 9 checks
#       Count L's
#       If checkL's == amountL's -> set the seat to #
#   If #: check all seats around it -> zeile-1 bis zeile+1, reihe-1 bis reihe+1 -> 9 checks
#       Count #'s -> amount#
#       count L's -> amountL's
#       amountSeats = count# + countL
#       If amountL >= 4 -> set seat to L
#
#Check all Seats again and count #


def changeSeats(oldAllSeats, loops):
    newAllSeats = copy.deepcopy(oldAllSeats)        #Copy list so that there is no "reference" to it
    for i in range(len(newAllSeats)):
        print(newAllSeats[i], end="\n")
        
    print("---")

    for row in range(len(allSeats)):
        for col in range(len(allSeats[row])):
            amountL = 0
            amountPound = 0
            checkSeats = 0
            currentSeat = oldAllSeats[row][col]

            def checkDirection(startRow, startCol, edgeRow, edgeCol, stepsRow, stepsCol):
                for tempRow in range(startRow, edgeRow, stepsRow):
                    for tempCol in range(startCol, edgeCol, stepsCol):
                        tempSeat = oldAllSeats[tempRow][tempCol]
                        if tempSeat == 'L':
                            return "L"
                        elif tempSeat == '#':
                            return "#"

            counter = 0
            while counter < 8:
                if counter == 0:
                    checkDirection(row-1, col-1, 0, 0, -1, -1)
                elif counter == 1:
                    checkDirection(row-1, col, 0, 0, -1, 0)
                elif counter == 2:
                    checkDirection(row-1, col+1, 0, len(oldAllSeats[row])-1, -1, +1)
                elif counter == 3:
                    checkDirection(row, col+1, len(oldAllSeats)-1, len(oldAllSeats[row])-1, 0, +1)
                elif counter == 4:
                    checkDirection(row+1, col+1, len(oldAllSeats)-1, len(oldAllSeats[row])-1, +1, +1)
                elif counter == 5:
                    checkDirection(row+1, col, len(oldAllSeats)-1, 0, +1, 0)
                elif counter == 6:
                    checkDirection()
                elif counter == 7:
                    checkDirection()

                counter += 1
                if symbol == 'L':
                    amountL += 1
                elif symbol == '#':
                    amountPound += 1

            '''for tempRow in range(-1, 0, 1):
                for tempCol in range(-1, 0, 1):
                    if tempRow == tempCol == 0:
                        continue

                    offset = 1
                    while 0 <= row+offset*tempRow < len(oldAllSeats) and 0 <= col+offset*tempCol < len(oldAllSeats[tempRow]):
                        tempSeat = oldAllSeats[row+offset*tempRow][col+offset*tempCol]
                        if tempSeat == 'L':
                            amountL += 1
                            tempRow += 1
                        elif tempSeat == '#':
                            amountPound += 1
                            tempRow += 1

                        offset += 1'''

            #Tast1
            '''for tempRow in range(row-1, row+2):
                for tempCol in range(col-1, col+2):
                    if tempRow != row or tempCol != col:
                        if tempRow >= 0 and tempCol >= 0 and tempRow < len(oldAllSeats) and tempCol < len(oldAllSeats[row]):
                            tempSeat = oldAllSeats[tempRow][tempCol]
                            if tempSeat == 'L':
                                amountL += 1
                            elif tempSeat == '#':
                                amountPound += 1'''
            #print(amountPound)
            checkSeats = amountL + amountPound

            #Use the current seat, amount of all seats, amount of L seats to see what needs to be changed
            if currentSeat == 'L' and checkSeats == amountL:
                newAllSeats[row][col] = '#'
            elif currentSeat == '#':
                #if amountPound >= 4:
                if amountPound >= 5:
                    newAllSeats[row][col] = 'L'

    if newAllSeats == oldAllSeats:
        occSeatCnt = 0
        for row in range(len(newAllSeats)):
            for col in range(len(newAllSeats[row])):
                if newAllSeats[row][col] == '#':
                    occSeatCnt += 1
        print(loops+1)
        print(occSeatCnt)
    else:
        loops += 1
        #print(loops)
        changeSeats(newAllSeats, loops)
        
loops = 0
changeSeats(allSeats, loops)

