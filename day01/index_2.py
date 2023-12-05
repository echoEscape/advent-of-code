input = open('input.txt', 'r')
lines = []
matchList = [1,2,3,4,5,6,7,8,9,"one","two","three","four","five","six","seven","eight","nine"]

#Split Lines of Input into its own array
for l in input:
    lines.append(l)
    
#Create multidimensional Array of length of the puzzle Input
numberOneList = []
numberTwoList = []

for line in lines:
    tempNumOne = 0
    tempNumTwo = 0
    #check each character of each line against the numbers 1-9
    for character in line:
        #check occurance of 1,2,3,4,5,6,7,8,9
        for number in matchList:
            if isinstance(number, int):
                #if a character of a line is a number 1-9 set tempValues to later fill array
                if character == str(number):
                    if tempNumOne == 0:
                        tempNumOne = number
                        #If only one number occurs in a line set the one occurance equal the first
                        tempNumTwo = number
                    else:
                        tempNumTwo = number
            else:
                try:
                    for i in range(len(number)):
                        pass
                except:
                    pass
                    

    numberOneList.append(tempNumOne)
    numberTwoList.append(tempNumTwo)

def convertToNumber(inputList):
    tempList = []
    for cnt in inputList:
        if inputList[cnt] == "one":
            tempList.append(1)
        elif inputList[cnt] == "two":
            tempList.append(2)
        elif inputList[cnt] == "three":
            tempList.append(3)
        elif inputList[cnt] == "four":
            tempList.append(4)
        elif inputList[cnt] == "five":
            tempList.append(5)
        elif inputList[cnt] == "six":
            tempList.append(6)
        elif inputList[cnt] == "seven":
            tempList.append(7)
        elif inputList[cnt] == "eight":
            tempList.append(8)
        elif inputList[cnt] == "nine":
            tempList.append(9)
        else:
            tempList.append(inputList[cnt])
    return tempList


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
    


