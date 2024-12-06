from itertools import permutations

input = open('input_01.txt', 'r')
lines = []
for l in input:
  lines.append(l.replace("\n", ""))

rules = lines[:lines.index("")]
pages = lines[lines.index("")+1:]

rulesList = []
for rule in rules:
  rulesList.append(rule.split("|"))

pagesList = []
for page in pages:
    pagesList.append(page.split(","))


def checkValidity(pages, rulesList):                                            # e.g. ['97', '13', '75', '29', '47'] and ['47', '29']
  occurrences = []
  valid = True
  for page in pages:                                                            # e.g. '97'
    for rules in rulesList:                                                     # e.g. ['47', '29'] from 47|29 <- incorrect btw because 29 cannot come before 47
      if page == rules[0] and rules[1] in occurrences:                                                         
          valid = False

    if valid:
      occurrences.append(page)

  if set(pages) == set(occurrences):
    return True, pages
  else:
    return False, pages
   

# Sadly doesn't work as it doesn't seem to generate all possible iterations of the page-orders -> endless loop
# Addendum: The idea in general was incorrect. I tried to use bubble sort even though I wanted to generate all permutations.
def bubbleSort(pages, rulesList):                                               # e.g. ['97', '13', '75', '29', '47']
  sortedList = False

  while not sortedList:
    sortedList = True
    for i in range(len(pages)-1):
      if checkValidity(pages, rulesList)[0] == False:                           
        sortedList = False
        pages[i], pages[i+1] = pages[i+1], pages[i] 
        
      else:
        return pages


# Task 1
correctRules = []
incorrectRules = []
for pages in pagesList:
  result = checkValidity(pages, rulesList)

  if result[0] == True:
    correctRules.append(result[1])
  elif result[0] == False:
    incorrectRules.append(result[1])

# Task 2
newSortedList = []
allVersions = []
for pages in incorrectRules:
  #newSortedList.append(bubbleSort(pages, rulesList))                           #Incorrectly used bubble sort even though I wanted all permutations
  
  # Foolishly thought that running all permutations wouldnt take that long. I was wrong.
  # The entire approach is flawed and needs to be thought through again.
  '''allVersions = list(permutations(pages))

  for version in allVersions:
    if checkValidity(version, rulesList)[0] == True:
      newSortedList.append(version)
  allVersions = []'''

# Solution calculation
solutionOne = 0
for pages in correctRules:
  middleIndex = len(pages) // 2
  solutionOne += int(pages[middleIndex])
print(solutionOne)

solutionTwo = 0
for pages in newSortedList:
  middleIndex = len(pages) // 2
  solutionTwo += int(pages[middleIndex])
print(solutionTwo)

        
        