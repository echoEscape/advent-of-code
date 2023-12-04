input = open('input1.txt', 'r')
lines = []
matchList = [1,2,3,4,5,6,7,8,9]

#Split Lines of Input into its own array
for l in input:
    lines.append(l)
    
#Create multidimensional Array of length of the puzzle Input
numberOneList = []
numberTwoList = []

iterationCnt = 0
for line in lines:
    tempNumOne = 0
    tempNumTwo = 0
    #check each character of each line against the numbers 1-9
    for character in line:
        #check occurance of 1,2,3,4,5,6,7,8,9
        for number in matchList:
            #if a character of a line is a number 1-9 set tempValues to later fill array
            if character == str(number):
                if tempNumOne == 0:
                    tempNumOne = number
                    #If only one number occurs in a line set the one occurance equal the first
                    tempNumTwo = number
                else:
                    tempNumTwo = number

    numberOneList.append(tempNumOne)
    numberTwoList.append(tempNumTwo)
    iterationCnt+=1

resultsList = []
tempString = ""
for cnt in range(len(numberOneList)):
    tempString = str(numberOneList[cnt])+str(numberTwoList[cnt])
    resultsList.append(tempString)
    tempString = ""

result = 0
counter = 0
for number in resultsList:
    #print(lines[counter])
    #print(number)
    result = result + int(number)
    counter += 1

print(result)
    


