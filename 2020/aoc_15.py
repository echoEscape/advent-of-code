#Hint: Takes a while to execute. It does work though.

puzzleInput = (12,20,0,6,1,17,7)
numCheck = puzzleInput[0]
answers = {}

for turn in range(0, 30000000):
    if turn < len(puzzleInput):                                                 
        answers[numCheck] = turn
        numCheck = puzzleInput[turn]                         

    elif numCheck not in answers:            
        answers[numCheck] = turn                                 
        numCheck = 0                                                           

    elif numCheck in answers:                                                     
        lastOccurance = answers[numCheck]
               
        #Add number from before with its previous turn to the list
        answers[numCheck] = turn

        #Search for new number by saying how many turns apart the number is from when it previously has been spoken
        numCheck = turn - lastOccurance

        
#print(answers)
print(numCheck)